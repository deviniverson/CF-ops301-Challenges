#!/bin/bash

# Script Name: clearlogs.sh
# Author: Devin Iverson
# Date of last revision: 05/02/22
# Purpose: Clear all logs that are present in array
# Variables: logfiles, file


# Main
logfiles=("syslog" "wtmp")

# for loop through log file names in declared list
for file in ${logfiles[@]};
do
    # print original log file
    cat /var/log/$file

    # clear log file
    truncate -s 0 /var/log/$file
    echo " "
    echo "$file Cleared!"

    # print cleared file
    cat /var/log/$file

    # create divider between iterations
    echo "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
done

# How can your script be used to clear your tracks?
# My script is easily adjusted to clear more log files. Just add or delete filenames within the logfiles array to match your desired files to be cleared.

# For each log cleared, explain what the log tracks in the Ubuntu system and why is this log important?
# syslog: Events from applications which do not have their own log file and all logs that used to be written in the file /var/log/messages.  
# wtmp: provides historical data of complete picture of user logins at which terminals, logouts, system events and current status of the system and system boot time
#
# 
