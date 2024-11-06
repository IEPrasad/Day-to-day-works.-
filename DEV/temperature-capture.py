import clr  # Ensure pythonnet is installed: pip install pythonnet
import time
from datetime import datetime, timedelta

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

    temperatures = []
    for i in range(len(handle.Hardware)):
        handle.Hardware[i].Update()
        for sensor in handle.Hardware[i].Sensors:
            if sensor.SensorType == Hardware.SensorType.Temperature:
                temperatures.append((sensor.Name, sensor.Value))

    if temperatures:
        for name, value in temperatures:
            print(f"{name}: {value}°C")
    else:
        print("Could not read CPU temperature.")

# Run the function every minute
while True:
    # Get the current time and format it
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    next_time = (now + timedelta(minutes=1)).strftime("%H:%M")
    current_date = now.strftime("%Y-%m-%d")

    # Display the date and time information
    print(f"\n--- Processor Temperature Readings for {current_date} ({current_time} - {next_time}) ---")
    
    # Get and display the CPU temperature
    get_cpu_temperature()
    
    # Wait 1 minute before the next reading
    print("Waiting 1 minute before the next reading...")
    time.sleep(60)  # Wait 60 seconds (1 minute)
