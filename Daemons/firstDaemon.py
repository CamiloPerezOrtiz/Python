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
import os.path as path
import subprocess
import commands
import socket
import time
import os
######End operating system libraries#####

pcName = socket.gethostname()

file = open('/home/hackematte/Desktop/hostName.txt', 'w')
file.write(pcName) #Change the pcś ip address on data document
file.close()

f = open('/home/hackematte/Desktop/clientName.txt', 'r') #Variable for client name
line=f.readline()
if line:
    name=line
f = open('/home/hackematte/Desktop/ipHost.txt', 'r') #Variable for ip address
line=f.readline()
if line:
    ip=line
f = open('/home/hackematte/Desktop/hostName.txt', 'r') #Variable for host name
line=f.readline()
if line:
    host=line

file = open('/home/hackematte/Desktop/clientInformation.txt', 'w')
file.write(host+"|"+ip+"|"+name+"|") #give the correct format to data document
file.close()

#####Start command section####
