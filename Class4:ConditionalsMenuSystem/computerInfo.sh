#!/bin/bash

# Script: computerInfo.sh
# Author: Devin Iverson
# Date of latest revision: 04/26/2022
# Purpose: Use conditionals and loops in Bash Scripting to provide user with computer information. Menu system used to allow user to choose what task is being requested.

# System Menu
menu(){
    echo " "
    echo "        MENU        "
    echo " "
    echo "
    Process_Name Process_Explanation
    ============ ===================
    HelloWorld  print_HelloWorld!_on_screen
    PingSelf  pings_this_computer's_loopback_address
    IPinfo  prints_network_adapter_information
    WhoAmI prints_username_of_current_user
    Exit  exit_from_program
    " | column -t
    echo " "
}


# Main
main(){
    while [ : ]
    do
        menu
        read -p 'Name of process: ' userinput

        if [ $userinput == 'HelloWorld' ] || [ $userinput == 'helloworld' ] || [ $userinput == 'HELLOWORLD' ]
        then
            echo "Hello World!"
            continue
        
        elif [ $userinput == 'PingSelf' ] || [ $userinput == 'pingself' ] || [ $userinput == 'PINGSELF' ]
        then
            ping 127.0.0.1 -c 5
            continue

        elif [ $userinput == 'IpInfo' ] || [ $userinput == 'ipinfo' ] || [ $userinput == 'IPINFO' ]
        then
            echo "$(ifconfig)"
            continue

        elif [ $userinput == 'WhoAmI' ] || [ $userinput == 'whoami' ] || [ $userinput == 'WHOAMI' ]
        then
            echo "$(whoami)"
            continue

        elif [ $userinput == 'Exit' ] || [ $userinput == 'exit' ] || [ $userinput == 'EXIT' ]
        then
            break

        else
            echo "Input doesn't match an available process. Please try again."
            continue
        
        fi
    done
}
main