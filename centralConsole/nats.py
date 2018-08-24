#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################
# This Code Has Been Developed By Jozic Espinoza AKA HackeMatte#
################################################################
# Start code #
##############

#####Operating System libraries#####
import subprocess
import os
import time
######End operating system libraries#####

#####Start variables section#####
Sq=0      #squid
Sq1=0     #squid1
Sq2=0     #squid2
Sq3=0     #squid3
Sq4=0     #squid4
Sq5=0     #squid5
Sq6=0     #squid6
SqA=0     #squidA
SqA1=0    #squidA1
SqA2=0    #squidA2
SqA3=0    #squidA3
SqA4=0    #squidA4
SqA5=0    #squidA5
SqA6=0    #squidA6
Sqg=0     #squidg
Sqg1=0    #squidg1
Sqg2=0    #squidg2
Sqg3=0    #squidg3
Sqg4=0    #squidg4
Sqg5=0    #squidg5
Sqg6=0    #squidg6
Sqg7=0    #squidg7
Sqg8=0    #squidg8
Sqg9=0    #squidg9
#####End variables section#####

#####Start XML labels section#####
#Words to search, it means, the xml labels for squid
label="<nat>"                     #Start label for nats
label1="<onetoone>"               #Start label for one to one nat
label2="</onetoone>"              #End label for one to one nat
label3="<outbound>"               #Start label for outbo8und nat
label4="</outbound>"              #End label for outbound nat
label5="</nat>"                   #End label for nats
labelA="<nat>"                    #Start label for nats
labelA1="<onetoone>"              #Start label for one to one nat
labelA2="</onetoone>"             #End label for one to one nat
labelA3="<outbound>"              #Start label for outbo8und nat
labelA4="</outbound>"             #End label for outbound nat
labelA5="</nat>"                  #End label for nats

####SquidGuard Section####
labelsq="<?xml version=\"1.0\"?>"  #Start label for XMLconfiguration file
label1sq="<nat>"                   #start nats label
label2sq="<outbound>"              #Start label for outbo8und nat
label3sq="</outbound>"             #End label for outbound nat
label4sq="</pfsense>"              #End label for XML configuration file

####Aux variables for increase the counter####
auxLabel="<separator>"
auxLabel1="</rule>"
#####End XML labels section#####

####Start user section####
#read rhe Xml User file

with open("config.xml") as f:
    for line in f:
        Sq += 1
        if label in line:
            squid = (Sq+1)
with open("config.xml") as f:
    for line in f:
        Sq1 += 1
        if label1 in line:
            squid1 = (Sq1)
            with open("config.xml") as f:
                for line in f:
                    Sq2 += 1
                    if auxLabel1 in line and Sq2 == squid1-1 :
                        squid2 = (Sq2)
with open("config.xml") as f:
    for line in f:
        Sq3 += 1
        if auxLabel1 in line and Sq3 == squid2 :
            squid3 = (Sq3)
with open("config.xml") as f:
    for line in f:
        Sq4 += 1
        if label3 in line:
            squid4 = (Sq4-1)
            squid5 = (Sq4+1)
with open("config.xml") as f:
    for line in f:
        Sq5 += 1
        if label4 in line:
            squid6 = (Sq5-1)

#command for cut an interval of speciffic lines and create a new file with those lines
#Nats user doc
command1  = 'sed \''+str(squid)+','+str(squid3)+' !d\' config.xml > natUser.xml'
os.system(command1)
#One to one user doc
command2  = 'sed \''+str(squid3+1)+','+str(squid4)+' !d\' config.xml > onetooneUser.xml'
os.system(command2)
#Outbound user doc
command3  = 'sed \''+str(squid5)+','+str(squid6)+' !d\' config.xml > outboundUser.xml'
os.system(command3)
####End user section####

###Start admin section####
with open("conf.xml") as f:
    for line in f:
        SqA += 1
        if labelA in line:
            squidA = (SqA+1)
with open("conf.xml") as f:
    for line in f:
        SqA1 += 1
        if labelA1 in line:
            squidA1 = (SqA1)
            with open("conf.xml") as f:
                for line in f:
                    SqA2 += 1
                    if auxLabel1 in line and SqA2 == squid1-1 :
                        squidA2 = (SqA2)
with open("conf.xml") as f:
    for line in f:
        SqA3 += 1
        if auxLabel1 in line and SqA3 == squid2 :
            squidA3 = (SqA3)
with open("conf.xml") as f:
    for line in f:
        SqA4 += 1
        if labelA3 in line:
            squidA4 = (SqA4-1)
            squidA5 = (SqA4+1)
with open("conf.xml") as f:
    for line in f:
        SqA5 += 1
        if labelA4 in line:
            squidA6 = (SqA5-1)

#command for cut an interval of speciffic lines and create a new file with those lines
#Nats admin doc
commandA1  = 'sed \''+str(squidA)+','+str(squidA3)+' !d\' conf.xml > natAdmin.xml'
os.system(commandA1)
commandA2  = 'sed \''+str(squidA3+1)+','+str(squidA4)+' !d\' conf.xml > onetooneAdmin.xml'
os.system(commandA2)
commandA3  = 'sed \''+str(squidA5)+','+str(squidA6)+' !d\' conf.xml > outboundAdmin.xml'
os.system(commandA3)
####End admin section####

####Start merge Section####
commandMix1='cat natUser.xml natAdmin.xml > finalNat.xml'
commandremoveU1 = 'rm -r -f natUser.xml'
commandremoveA1 = 'rm -r -f natAdmin.xml'
os.system(commandMix1)
os.system(commandremoveU1)
os.system(commandremoveA1)
commandMix2='cat onetooneUser.xml onetooneAdmin.xml > finalOnetoone.xml'
commandremoveU2 = 'rm -r -f onetooneUser.xml'
commandremoveA2 = 'rm -r -f onetooneAdmin.xml'
os.system(commandMix2)
os.system(commandremoveU2)
os.system(commandremoveA2)
commandMix3='cat outboundUser.xml outboundAdmin.xml > finalOutbound.xml'
commandremoveU3 = 'rm -r -f outboundUser.xml'
commandremoveA3 = 'rm -r -f outboundAdmin.xml'
os.system(commandMix3)
os.system(commandremoveU3)
os.system(commandremoveA3)
#####End merge section#####

#####Start get final document section#####
with open("config.xml") as f:
    for line in f:
        Sqg += 1
        if labelsq in line:
            squidg = (Sqg)
with open("config.xml") as f:
    for line in f:
        Sqg1 += 1
        if label1sq in line:
            squidg1 = (Sqg1)
with open("config.xml") as f:
    for line in f:
        Sqg2 += 1
        if label2sq in line:
            squidg2 = (Sqg2)
with open("config.xml") as f:
    for line in f:
        Sqg3 += 1
        if label3sq in line:
            squidg3 = (Sqg3)
with open("config.xml") as f:
    for line in f:
        Sqg4 += 1
        if label4sq in line:
            squidg4 = (Sqg4)


#before nat doc
commandsq1  = 'sed \''+str(squidg)+','+str(squidg1)+' !d\' config.xml > beforeNat.xml'
os.system(commandsq1)
#before outbound doc
commandsq2  = 'sed \''+str(squidg2)+','+str(squidg2)+' !d\' config.xml > beforeOutbound.xml'
os.system(commandsq2)
#before End doc
commandsq3  = 'sed \''+str(squidg3)+','+str(squidg4)+' !d\' config.xml > beforeEnd.xml'
os.system(commandsq3)
#####End get final document section#####

####Start semifinal merge Section####
commandMixsq='cat beforeNat.xml finalNat.xml > finalsq.xml'
commandremovesq = 'rm -r -f beforeNat.xml'
commandremovesqg = 'rm -r -f finalNat.xml'
os.system(commandMixsq)
os.system(commandremovesq)
os.system(commandremovesqg)
commandMixsq3='cat beforeOutbound.xml finalOutbound.xml > finalsq1.xml'
commandremovesq3 = 'rm -r -f beforeOutbound.xml'
commandremovesqg3 = 'rm -r -f finalOutbound.xml'
os.system(commandMixsq3)
os.system(commandremovesq3)
os.system(commandremovesqg3)
#####End semifinal merge section#####

#####Start final merge Section#####
commandMixfsq1 = 'cat finalsq.xml finalOnetoone.xml > finalmix1.xml'
commandremovefsq1 = 'rm -r -f finalsq.xml'
commandremovefsqg1 = 'rm -r -f finalOnetoone.xml'
os.system(commandMixfsq1)
os.system(commandremovefsq1)
os.system(commandremovefsqg1)
commandMixfsq2 = 'cat finalmix1.xml finalsq1.xml > finalmix2.xml'
commandremovefsq2 = 'rm -r -f finalmix1.xml'
commandremovefsqg2 = 'rm -r -f finalsq1.xml'
os.system(commandMixfsq2)
os.system(commandremovefsq2)
os.system(commandremovefsqg2)
commandMixfsq3 = 'cat finalmix2.xml beforeEnd.xml > finalmix3.xml'
commandremovefsq3 = 'rm -r -f finalmix2.xml'
commandremovefsqg3 = 'rm -r -f beforeEnd.xml'
os.system(commandMixfsq3)
os.system(commandremovefsq3)
os.system(commandremovefsqg3)
#####End finalMerge section#####

commandDelete1 = 'rm -r -f conf.xml'
commandDelete2 = 'rm -r -f config.xml'
commandDelete3 = 'mv finalmix3.xml config.xml'
os.system(commandDelete1)
os.system(commandDelete2)
os.system(commandDelete3)
