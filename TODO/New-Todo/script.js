const { createApp } = Vue;

createApp({
    data() {
        return {
            targetHours: 8,
            tasks: [
                {
                    id: 1,
                    name: "Example Task",
                    priority: "Medium",
                    startDate: new Date().toISOString().split('T')[0],
                    endDate: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                    progress: 0,
                    timeRemaining: "7 days 0 hours 0min",
                    isDone: false
                }
            ],
            timeSlots: {},
            newTask: {
                name: "",
                startDate: "",
                endDate: "",
                priority: "Medium",
                progress: 0,
                isDone: false
            },
            editingTask: false,
            editingTaskId: null,
            showProgressModal: false,
            tempProgress: 0,
            selectedTask: null,
            currentEditingSlot: null,
            isDragging: false,
            startX: 0,
            currentSlotWidth: 0,
            dragStartTime: 0
        };
    },
    computed: {
        currentDate() {
            return new Date().toLocaleDateString('en-US', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
        },
        currentTime() {
            return new Date().toLocaleTimeString('en-US', {
                hour: '2-digit',
                minute: '2-digit'
            });
        },
        totalWorkedMinutes() {
            return Object.values(this.timeSlots).reduce((total, slot) => {
                return total + (slot.minutes || 0);
            }, 0);
        },
        totalWorkedTime() {
            const totalMinutes = this.totalWorkedMinutes;
            const hours = Math.floor(totalMinutes / 60);
            const minutes = totalMinutes % 60;
            return `${hours}h ${minutes}m`;
        },
        totalBreakTime() {
            const totalPossibleMinutes = this.targetHours * 60;
            const breakMinutes = Math.max(0, totalPossibleMinutes - this.totalWorkedMinutes);
            const hours = Math.floor(breakMinutes / 60);
            const minutes = breakMinutes % 60;
            return `${hours}h ${minutes}m`;
        },
        remainingTime() {
            const targetMinutes = this.targetHours * 60;
            const remainingMinutes = Math.max(0, targetMinutes - this.totalWorkedMinutes);
            const hours = Math.floor(remainingMinutes / 60);
            const minutes = remainingMinutes % 60;
            return `${hours}h ${minutes}m`;
        },
        completionRate() {
            const completed = this.tasks.filter(task => task.isDone).length;
            return this.tasks.length > 0 ? Math.round((completed / this.tasks.length) * 100) : 0;
        },
        hoursArray() {
            return Array.from({ length: 24 }, (_, i) => i);
        },
        activeTimeSlots() {
            return Object.entries(this.timeSlots)
                .filter(([_, slot]) => slot.isWorking)
                .length;
        }
    },
    methods: {
        formatHour(hour) {
            return `${String(hour).padStart(2, '0')}:00`;
        },
        formatDate(date) {
            return new Date(date).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'short',
                day: 'numeric'
            });
        },
        initializeTimeSlot(hour) {
            if (!this.timeSlots[hour]) {
                this.timeSlots[hour] = {
                    minutes: 0,
                    isWorking: false,
                    notes: '',
                    startX: 0,
                    currentWidth: 0
                };
            }
        },
        startDragging(event, hour) {
            // Ensure the slot exists and is working
            if (!this.timeSlots[hour]?.isWorking) return;
            
            this.isDragging = true;
            this.currentEditingSlot = hour;
            
            const timeBlock = event.currentTarget;
            const rect = timeBlock.getBoundingClientRect();
            
            this.startX = event.clientX - rect.left;
            this.dragStartTime = this.timeSlots[hour].minutes;
            
            // Add event listeners for drag
            document.addEventListener('mousemove', this.handleDrag);
            document.addEventListener('mouseup', this.stopDragging);
            
            // Prevent text selection while dragging
            event.preventDefault();
        },

        handleDrag(event) {
            if (!this.isDragging || this.currentEditingSlot === null) return;
            
            const timeBlock = document.querySelector(`[data-hour="${this.currentEditingSlot}"] .time-block`);
            if (!timeBlock) return;
            
            const rect = timeBlock.getBoundingClientRect();
            const offsetX = event.clientX - rect.left;
            const width = rect.width;
            
            // Calculate minutes based on the drag position
            const percentage = Math.max(0, Math.min(100, (offsetX / width) * 100));
            const minutes = Math.round((percentage / 100) * 60);
            
            this.updateTimeSlot(this.currentEditingSlot, minutes);
        },

        stopDragging() {
            if (this.isDragging) {
                this.isDragging = false;
                this.currentEditingSlot = null;
                document.removeEventListener('mousemove', this.handleDrag);
                document.removeEventListener('mouseup', this.stopDragging);
            }
        },

        toggleTimeSlot(hour) {
            this.initializeTimeSlot(hour);
            const slot = this.timeSlots[hour];
            
            if (!slot.isWorking) {
                // Activating the slot
                slot.isWorking = true;
                slot.minutes = slot.minutes || 30; // Default to 30 minutes if no time set
            } else {
                // Deactivating the slot if minutes are 0
                if (slot.minutes === 0) {
                    slot.isWorking = false;
                }
            }
            
            this.currentEditingSlot = hour;
            this.saveToLocalStorage();
        },

        updateTimeSlot(hour, minutes) {
            this.initializeTimeSlot(hour);
            let value = parseInt(minutes);
            
            // Validate input
            if (isNaN(value)) value = 0;
            if (value < 0) value = 0;
            if (value > 60) value = 60;
            
            // Update the time slot
            this.timeSlots[hour].minutes = value;
            this.timeSlots[hour].isWorking = value > 0;
            
            // Save changes
            this.saveToLocalStorage();
        },

        getSlotStyle(hour) {
            const slot = this.timeSlots[hour];
            if (!slot || !slot.isWorking) return {};
            
            return {
                backgroundColor: '#7289da33',
                position: 'relative',
                cursor: 'ew-resize',
                userSelect: 'none',
                height: '40px', // Add fixed height for better dragging
                borderRadius: '4px',
                transition: 'background-color 0.2s ease'
            };
        },

        getProgressStyle(hour) {
            const slot = this.timeSlots[hour];
            if (!slot || !slot.isWorking) return { width: '0%' };
            
            const width = (slot.minutes / 60) * 100;
            return {
                width: `${width}%`,
                backgroundColor: '#7289da',
                position: 'absolute',
                height: '100%',
                left: 0,
                top: 0,
                borderRadius: '4px',
                transition: 'width 0.1s ease'
            };
        },
        addNoteToTimeSlot(hour, note) {
            this.initializeTimeSlot(hour);
            this.timeSlots[hour].notes = note;
        },
        startEditTask(task) {
            this.editingTask = true;
            this.editingTaskId = task.id;
            this.newTask = { ...task };
        },
        cancelEdit() {
            this.editingTask = false;
            this.editingTaskId = null;
            this.resetForm();
        },
        resetForm() {
            this.newTask = {
                name: "",
                startDate: "",
                endDate: "",
                priority: "Medium",
                progress: 0,
                isDone: false
            };
        },
        saveTask() {
            if (!this.newTask.name || !this.newTask.startDate || !this.newTask.endDate) {
                alert('Please fill in all required fields');
                return;
            }

            if (this.editingTask) {
                const index = this.tasks.findIndex(t => t.id === this.editingTaskId);
                if (index !== -1) {
                    this.tasks[index] = {
                        ...this.newTask,
                        id: this.editingTaskId,
                        timeRemaining: this.calculateTimeRemaining(this.newTask.endDate)
                    };
                }
                this.editingTask = false;
                this.editingTaskId = null;
            } else {
                this.tasks.push({
                    id: Date.now(),
                    ...this.newTask,
                    timeRemaining: this.calculateTimeRemaining(this.newTask.endDate)
                });
            }

            this.resetForm();
            this.saveToLocalStorage();
        },
        deleteTask(task) {
            if (confirm('Are you sure you want to delete this task?')) {
                const index = this.tasks.findIndex(t => t.id === task.id);
                if (index !== -1) {
                    this.tasks.splice(index, 1);
                    this.saveToLocalStorage();
                }
            }
        },
        toggleTaskDone(task) {
            const index = this.tasks.findIndex(t => t.id === task.id);
            if (index !== -1) {
                this.tasks[index].isDone = !this.tasks[index].isDone;
                this.tasks[index].progress = this.tasks[index].isDone ? 100 : 0;
                this.saveToLocalStorage();
            }
        },
        showProgressEdit(task) {
            this.selectedTask = task;
            this.tempProgress = task.progress;
            this.showProgressModal = true;
        },
        saveProgress() {
            if (this.selectedTask) {
                const index = this.tasks.findIndex(t => t.id === this.selectedTask.id);
                if (index !== -1) {
                    this.tasks[index].progress = this.tempProgress;
                    if (this.tempProgress === 100) {
                        this.tasks[index].isDone = true;
                    }
                    this.saveToLocalStorage();
                }
            }
            this.closeProgressModal();
        },
        closeProgressModal() {
            this.showProgressModal = false;
            this.selectedTask = null;
            this.tempProgress = 0;
        },
        calculateTimeRemaining(endDate) {
            const end = new Date(endDate);
            const now = new Date();
            const diff = end - now;
            
            if (diff <= 0) return "Overdue";
            
            const days = Math.floor(diff / (1000 * 60 * 60 * 24));
            const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
            
            return `${days} days ${hours} hours ${minutes}min`;
        },
        saveTargetHours(value) {
            this.targetHours = Math.max(1, Math.min(24, parseInt(value) || 8));
            this.saveToLocalStorage();
        },
        saveToLocalStorage() {
            localStorage.setItem('taskManagerData', JSON.stringify({
                timeSlots: this.timeSlots,
                tasks: this.tasks,
                targetHours: this.targetHours
            }));
        }
    },
    mounted() {
        // Initialize timeSlots for all hours
        this.hoursArray.forEach(hour => {
            this.initializeTimeSlot(hour);
        });

        // Update current time every minute
        setInterval(() => {
            this.$forceUpdate();
        }, 60000);
        
        // Update time remaining for tasks every minute
        setInterval(() => {
            this.tasks.forEach((task, index) => {
                if (!task.isDone) {
                    this.tasks[index].timeRemaining = this.calculateTimeRemaining(task.endDate);
                }
            });
        }, 60000);

        // Load saved data from localStorage if available
        const savedData = localStorage.getItem('taskManagerData');
        if (savedData) {
            const data = JSON.parse(savedData);
            this.timeSlots = data.timeSlots || {};
            this.tasks = data.tasks || [];
            this.targetHours = data.targetHours || 8;
        }
    }
}).mount('#app');