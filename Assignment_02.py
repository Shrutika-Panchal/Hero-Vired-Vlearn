import psutil
import time

print("Monitoring CPU usage...")

# Monitoring CPU usage continuously
while True:
    cpu_usage = psutil.cpu_percent()

    # Display CPU Usage
    if cpu_usage < 80:
        
        print("CPU usage normal: ("+ str(cpu_usage) + "%)")
    
    # If CPU usage exceeds threshold
    else :
         print("Alert! CPU usage exceeds threshold: ("+ str(cpu_usage) + "%)")   

    # Wait for 1 second before checking the CPU usage again
    time.sleep(1)
