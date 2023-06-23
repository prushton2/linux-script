import subprocess
from tabulate import tabulate
import colorama

devices = subprocess.run("cat /sys/class/thermal/cooling_device*/type", capture_output=True, shell=True)
devices = devices.stdout.decode().split("\n")
zones = subprocess.run("cat /sys/class/thermal/thermal_zone*/type", capture_output=True, shell=True)
zones = zones.stdout.decode().split("\n")
temps = subprocess.run("cat /sys/class/thermal/thermal_zone*/temp", capture_output=True, shell=True)
temps = temps.stdout.decode().split("\n")

#For some reason the last element doesnt exist?
temps = temps[0:-1]

devices += [''] * (len(zones)-len(devices))

table = []

for i, j in enumerate(temps):
    table.append([zones[i], int(temps[i])/1000, ""])

for i, j in enumerate(table):
    color = None
    warning = " "
    if(table[i][1] < 50):
        color = colorama.Fore.GREEN
    elif(table[i][1] < 70):
         color = colorama.Fore.YELLOW
    else:
        color = colorama.Fore.RED
        warning = "!!"

    table[i][2] = warning + colorama.Fore.RESET
    table[i][1] = color + str(table[i][1])

print(tabulate(table, headers=["Zone", "Temp (C)", ""]))
