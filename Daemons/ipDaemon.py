#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################
# This Code Has Been Developed By Jozic Espinoza AKA HackeMatte#
################################################################
# Start code #
##############

###############################################################
# All routes must be changed, these routes only are for test  #
# this script, the correct route will be the local from the   #
# user's PC                                                   #
###############################################################

###############################################################
# The replace command must make all changes into central      #
# console with ssh connection                                 #
###############################################################

#####Operating System libraries#####
from daemon import runner #python-daemon library
import os.path as path
import subprocess
import commands
import logging
import socket
import time
import os
#####End Operating System libraries# section####

if (path.exists("/home/hackematte/Desktop/firstDaemon.py")):
    command="python /home/hackematte/Desktop/menu.py"
    os.system(command)
    command1="python /home/hackematte/Desktop/firstDaemon.py"
    os.system(command1)
    removeCommand="rm -r -f /home/hackematte/Desktop/menu.py"
    removeCommand1="rm -r -f /home/hackematte/Desktop/firstDaemon.py"
    os.system(removeCommand)
    os.system(removeCommand1)
else:
    command2="python /home/hackematte/Desktop/getipDaemon.py"
