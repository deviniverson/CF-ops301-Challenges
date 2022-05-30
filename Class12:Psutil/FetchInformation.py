#!/usr/bin/env python3

# File Name: FetchInformation.py
# Author: Devin Iverson
# Date: 05/26/2022
# Purpose: 
import psutil

# 
cpu_times = psutil.cpu_times(percpu=True)
print(cpu_times)
#print(psutil.cpu_times(percpu=True))
# ctx_switches: # of context switches, interrupts: # of interrupts, soft_interrupts: # of software interrupts
cpu_stats = psutil.cpu_stats()

# print time spent by normal processes executing
print("CPU time spent by normal processes: ", cpu_times[0])

# print time spent by processes executing in kernel mode
print("CPU time spent by processes in kernel mode: ", cpu_times[2])

# print time when system was idle
print("CPU time spent with system is idle: ", cpu_times[3])

# print time spent by priority processes executing
print("CPU time spent by priority processes: ", cpu_times[1])

# print time spent waiting for I/O to complete
"CPU time spent waiting for I/O to complete: ", 

# print time spent for servicing hardware interrupts
"CPU time spent for servicing hardare interrupts: ", 

# print time spent for servicing software interrupts
"CPU time spent for servicing software interrupts: ", 

# print time spent by other operating systems running in a virtualized environment
"CPU time spent for other operating systems running in a virtualized environment: ", 

# print time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
"CPU time spent running a virtual CPU for guest operating systems under the Linux kernel: ", 

# Stretch Goals

# Save the information to a .txt file


# Email the .txt file to yourself using Sendmail.