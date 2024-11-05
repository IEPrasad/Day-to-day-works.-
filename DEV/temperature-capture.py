import psutil

def get_cpu_temperature():
    # Check if the sensor data for temperature is available
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        if "coretemp" in temps:
            # On Linux, you may get the "coretemp" readings
            for entry in temps["coretemp"]:
                print(f"{entry.label or 'CPU'} temperature: {entry.current}°C")
        elif "cpu-thermal" in temps:
            # On Raspberry Pi or ARM devices, you may get "cpu-thermal"
            for entry in temps["cpu-thermal"]:
                print(f"{entry.label or 'CPU'} temperature: {entry.current}°C")
        else:
            print("Temperature sensors not available on this system.")
    else:
        print("Temperature sensors not supported on this platform.")

# Run the function
get_cpu_temperature()
