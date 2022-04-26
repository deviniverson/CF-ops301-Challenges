#!/bin/bash

# Author:                       Devin Iverson
# Course Code:                  301n2
# Script:                       DateTimeLog.sh
# Purpose:                      Copy system log and rename filename with date and time appended at the end

cp /var/log/syslog 'syslog_$(date +%D_%T)'