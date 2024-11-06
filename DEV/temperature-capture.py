import clr  # Ensure pythonnet is installed: pip install pythonnet
import time
from datetime import datetime, timedelta
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["hardware_monitor"]  # Database name
collection = db["cpu_temperatures"]  # Collection name

# Path to OpenHardwareMonitorLib.dll
dll_path = r"E:\openhardwaremonitor-v0.9.6\OpenHardwareMonitor\OpenHardwareMonitorLib.dll"

# Load the OpenHardwareMonitorLib.dll file
clr.AddReference(dll_path)
from OpenHardwareMonitor import Hardware

def get_cpu_temperature():
    # Initialize the OpenHardwareMonitor
    handle = Hardware.Computer()
    handle.CPUEnabled = True  # Enable CPU sensors
    handle.Open()

    # Variables to store specific temperature readings
    core1_temp = None
    core2_temp = None
    package_temp = None

    # Iterate through hardware sensors to find the specific ones
    for i in range(len(handle.Hardware)):
        handle.Hardware[i].Update()
        for sensor in handle.Hardware[i].Sensors:
            if sensor.SensorType == Hardware.SensorType.Temperature:
                if sensor.Name == "CPU Core #1":
                    core1_temp = sensor.Value
                elif sensor.Name == "CPU Core #2":
                    core2_temp = sensor.Value
                elif sensor.Name == "CPU Package":
                    package_temp = sensor.Value

    # Prepare data dictionary with the specific core and package temperatures
    data = {
        "timestamp": datetime.now(),
        "CPU Core #1": core1_temp,
        "CPU Core #2": core2_temp,
        "CPU Package": package_temp
    }

    # Insert data into MongoDB
    collection.insert_one(data)
    print("Data inserted into MongoDB:", data)

# Run the function every minute
while True:
    # Get the current time and format it
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    next_time = (now + timedelta(minutes=1)).strftime("%H:%M")
    current_date = now.strftime("%Y-%m-%d")

    # Display the date and time information
    print(f"\n--- Processor Temperature Readings for {current_date} ({current_time} - {next_time}) ---")
    
    # Get and display the CPU temperature and save to MongoDB
    get_cpu_temperature()
    
    # Wait 1 minute before the next reading
    print("Waiting 1 minute before the next reading...")
    time.sleep(10)  # Wait 10 seconds (1 minute)
