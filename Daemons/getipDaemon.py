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

############################################################################################################################
# The replace command must make all changes into central                                                                   #
# console with ssh connection                                                                                              #
#                                                                                                                          #
# HOST REFERS TO CLIENT                                                                                                    #
# LOCAL REFERS TO CENTRAL CONSOLE                                                                                          #
#                                                                                                                          #
# COMMAND TO REPLACE IP LINE                                                                                               #
# ssh hackematte@192.168.0.17 'sed -i 's/nestle/Warriors/g' /home/hackematte/Desktop/clientInformation.txt\'               #
# ssh <local user>@<local ip> 'sed -i 's/<originalword>/<replaceword>/g' <local route from file>'                          #
#                                                                                                                          #
# COMMAND TO VERIFY FILE EXISTENCE                                                                                         #
# ssh hackematte@192.168.0.17 '[ -f /home/hackematte/Desktop/clientInformation.txt ] && echo "Existe" || echo "No existe"' #
# ssh <local user>@<local ip> '[ -f <local direction FILE> ] && echo "Existe" || echo "No existe"'                         #
#                                                                                                                          #
# COMMAND TO VERIFY FOLDER EXISTENCE                                                                                       #
# ssh hackematte@192.168.0.17 '[ -d /home/hackematte/Desktop/Directory ] && echo "Existe" || echo "No existe"'             #
# ssh <local user>@<local ip> '[ -d <local direction DIRECTORY> ] && echo "Existe" || echo "No existe"'                    #
#                                                                                                                          #
# COMMAND TO SET A FILE REMOTELY                                                                                           #
# scp /cf/conf/config.xml hackematte@192.168.0.17:/home/hackematte/Desktop/config.xml                                      #
# scp <host route> <local user>@<ip local>:<final route local>                                                             #
#                                                                                                                          #
# COMMAND TO GET A FILE REMOTELY                                                                                           #
# scp hackematte@192.168.0.17:/home/hackematte/Desktop/config.xml /cf/conf/config.xml                                      #
# scp <local user>@<ip local>:<local route> <final host route>                                                             #
############################################################################################################################

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


class App():
    def __init__(self):
        self.stdin_path      = '/dev/null' #Standard enter
        self.stdout_path     = '/dev/tty'  #Standard exit
        self.stderr_path     = '/dev/tty'
        self.pidfile_path    = '/var/run/test.pid' #Daemon PId route
        self.pidfile_timeout = 5

    def run(self): #To execute in backround

        while True:

            pcName = socket.gethostname()
            f = open('/home/hackematte/Desktop/interfaceName.txt', 'r')
            line=f.readline()
            if line:
                interfaceName=line
            ipCommand="ifconfig "+str(interfaceName)+" | grep \"inet addr\" | cut -d ':' -f 2 | cut -d ' ' -f 1"
            ipAddress=commands.getoutput(ipCommand)

            #The firstDaemon.py script only will be execute the first time, after that
            #the firstDaemon.py will be deleted from host PC

            if (path.exists("/home/hackematte/Desktop/firstDaemon.py")):
                command="python /home/hackematte/Desktop/firstDaemon.py"
                os.system(command)
                removeCommand="rm -r -f /home/hackematte/Desktop/firstDaemon.py"
                os.system(removeCommand)

            #When the firstDaemon.py script was deleted start de comparison section
            else:
                f = open('/home/hackematte/Desktop/ipHost.txt', 'r')
                line=f.readline()
                if line:
                    commandline=line
                    if commandline==ipAddress:
                        pass
                    else:
                        previousIP=commandline[:-1]
                        newIp=ipAddress
                        file = open('/home/hackematte/Desktop/ipHost.txt', 'w')
                        file.write(newIp) #Write de pc's new ip address
                        file.close()
                        replacementCommand  ="sed -i \'s/"+str(previousIP)+"/"+str(newIp)+"/g\' \"/home/hackematte/Desktop/clientInformation.txt\"" #Change the pcś ip address on data document
                        os.system(replacementCommand)
                f = open('/home/hackematte/Desktop/hostName.txt', 'r')
                line=f.readline()
                if line:
                    commandline=line
                    if commandline==pcName:
                        pass
                    else:
                        previousHostname=commandline[:-1]
                        newHostname=pcName
                        file = open('/home/hackematte/Desktop/hostName.txt', 'w')
                        file.write(pcName) #Write de pc's new hostname
                        file.close()
                        replacementCommand  ="sed -i \'s/"+str(previousHostname)+"/"+str(newHostname)+"/g\' \"/home/hackematte/Desktop/clientInformation.txt\"" #Change the hostname on data document
                        os.system(replacementCommand)

if __name__ == '__main__':
    app = App()    #Instances
    logger = logging.getLogger("testlog")  #create the daemon's binnacle
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(" ")
    handler = logging.FileHandler("/var/log/test.log") #binnacle route
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    #call the daemon instances
    serv = runner.DaemonRunner(app)
    serv.daemon_context.files_preserve=[handler.stream]
    serv.do_action() #To execute metode from app object
