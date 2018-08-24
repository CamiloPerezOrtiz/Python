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
groupName = raw_input("Enter the group name to create database: ")
interfaceName = raw_input("Enter the network interface name to start diagnostic: ")
file = open('/home/hackematte/Desktop/interfaceName.txt', 'w')
file.write(interfaceName) #Change the hostname on data document
file.close()
file = open('/home/hackematte/Desktop/clientName.txt', 'w')
file.write(groupName) #Change the hostname on data document
file.close()
ipCommand="ifconfig "+str(interfaceName)+" | grep \"inet addr\" | cut -d ':' -f 2 | cut -d ' ' -f 1"
getIp=commands.getoutput(ipCommand)
file = open('/home/hackematte/Desktop/ipHost.txt', 'w')
file.write(getIp) #Change the hostname on data document
file.close()
