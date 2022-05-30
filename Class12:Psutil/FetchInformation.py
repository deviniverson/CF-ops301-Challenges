#!/usr/bin/env python3

# File Name: FetchInformation.py
# Author: Devin Iverson
# Date: 05/26/2022
# Purpose: 
import psutil

# 
cpu_times = psutil.cpu_times()

#print(cpu_times)

# print time spent by normal processes executing
print("CPU time spent by normal processes: ", cpu_times[0])

# print time spent by processes executing in kernel mode
print("CPU time spent by processes in kernel mode: ", cpu_times[2])

# print time when system was idle
print("CPU time spent with system is idle: ", cpu_times[3])

# print time spent by priority processes executing
print("CPU time spent by priority processes: ", cpu_times[1])

# print time spent waiting for I/O to complete
print("CPU time spent waiting for I/O to complete: ", cpu_times[4]) 

# print time spent for servicing hardware interrupts
print("CPU time spent for servicing hardare interrupts: ", cpu_times[5])

# print time spent for servicing software interrupts
print("CPU time spent for servicing software interrupts: ", cpu_times[6])

# print time spent by other operating systems running in a virtualized environment
print("CPU time spent for other operating systems running in a virtualized environment: ", cpu_times[7])

# print time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print("CPU time spent running a virtual CPU for guest operating systems under the Linux kernel: ", cpu_times[8])

# Stretch Goals

# Save the information to a .txt file


# Email the .txt file to yourself using Sendmail.