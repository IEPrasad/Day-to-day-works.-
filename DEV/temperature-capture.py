import clr  # Make sure pythonnet is installed: pip install pythonnet
import os

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

# Run the function
get_cpu_temperature()
