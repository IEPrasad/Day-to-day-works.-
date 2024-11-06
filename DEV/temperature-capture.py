import clr  # Make sure pythonnet is installed: pip install pythonnet
import time
from datetime import datetime

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

def display_temperatures():
    now = datetime.now()
    print(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    temperatures = get_cpu_temperature()
    if temperatures:
        for name, value in temperatures:
            if value is not None:
                print(f"{name}: {value:.1f}°C")
            else:
                print(f"{name}: N/A")
    else:
        print("Could not read CPU temperature.")
    
    print("-" * 50)
    print("\n")

# Run the function every minute for continuous monitoring
while True:
    display_temperatures()
    time.sleep(10)  # Delay for 1 minute before the next reading
