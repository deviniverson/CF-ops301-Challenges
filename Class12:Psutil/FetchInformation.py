#!/usr/bin/env python3

# File Name: FetchInformation.py
# Author: Devin Iverson
# Date: 05/26/2022
# Purpose: 
import psutil

# 
cpu_times = psutil.cpu_times()

# ctx_switches: # of context switches, interrupts: # of interrupts, soft_interrupts: # of software interrupts
cpu_stats = psutil.cpu_stats()

# print time spent by normal processes executing


# print time spent by processes executing in kernel mode


# print time when system was idle


# print time spent by priority processes executing


# print time spent waiting for I/O to complete


# print time spent for servicing hardware interrupts


# print time spent for servicing software interrupts


# print time spent by other operating systems running in a virtualized environment


# print time spent running a virtual CPU for guest operating systems under the control of the Linux kernel


# Stretch Goals

# Save the information to a .txt file


# Email the .txt file to yourself using Sendmail.