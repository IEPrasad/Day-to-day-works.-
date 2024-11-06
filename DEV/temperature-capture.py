import clr  # Make sure pythonnet is installed: pip install pythonnet
import time
from datetime import datetime
from pymongo import MongoClient

# MongoDB configuration
mongo_client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI if needed
db = mongo_client["hardware_monitor"]
collection = db["cpu_temperatures"]

# Path to the OpenHardwareMonitorLib.dll file
dll_path = r"E:\openhardwaremonitor-v0.9.6\OpenHardwareMonitor\OpenHardwareMonitorLib.dll"

# Load the OpenHardwareMonitorLib.dll
clr.AddReference(dll_path)
from OpenHardwareMonitor import Hardware

def get_cpu_temperature():
    # Initialize OpenHardwareMonitor
    computer = Hardware.Computer()
    computer.CPUEnabled = True
    computer.Open()

    # Collect temperatures for each CPU core and the CPU package
    temperatures = []
    for hardware in computer.Hardware:
        hardware.Update()
        for sensor in hardware.Sensors:
            if sensor.SensorType == Hardware.SensorType.Temperature:
                temperatures.append((sensor.Name, sensor.Value))
    
    return temperatures if temperatures else None

def display_and_log_temperatures():
    now = datetime.now()
    print(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    temperatures = get_cpu_temperature()
    if temperatures:
        temperature_data = {"timestamp": now, "temperatures": []}
        for name, value in temperatures:
            if value is not None:
                print(f"{name}: {value:.1f}°C")
                temperature_data["temperatures"].append({"sensor_name": name, "temperature": value})
            else:
                print(f"{name}: N/A")
        
        # Insert the temperature data into MongoDB
        collection.insert_one(temperature_data)
        print("Temperature data logged to MongoDB.")
    else:
        print("Could not read CPU temperature.")
    
    print("-" * 50)
    print("\n")

# Run the function every minute for continuous monitoring
while True:
    display_and_log_temperatures()
    time.sleep(10)  # Delay for 10 seconds before the next reading
