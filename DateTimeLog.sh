#!/bin/bash

# Author:                       Devin Iverson
# Course Code:                       301n2
# Script:                       DateTimeLog.sh
# Purpose:                      Copy system log and rename filename with date and time appended at the end

# define date and time as variable
now='date +"%D_%T"'



# copy log file and rename it with date and time in filename
#log={cp /var/log/system.log .}

echo ${now}
# rename log file
#mv "$log" "system.log"