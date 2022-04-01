from json import loads
import os
import psutil

load, loads, load15 = psutil.getloadavg()

cpu_usage = (load15/os.cpu_count()) * 100

print("The CPU usage is : ", cpu_usage)