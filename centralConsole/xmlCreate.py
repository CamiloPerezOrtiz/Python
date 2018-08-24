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
Sq7=0     #squid7
Sq8=0     #squid8
Sq9=0     #squid9
Sq10=0    #squid10
Sq11=0    #squid11
Sq12=0    #squid12
Sq13=0    #squid13
Sq14=0    #squid14
Sq15=0    #squid15
SqA=0     #squidA
SqA1=0    #squidA1
SqA2=0    #squidA2
SqA3=0    #squidA3
SqA4=0    #squidA4
SqA5=0    #squidA5
SqA6=0    #squidA6
SqA7=0    #squidA7
SqA8=0    #squidA8
SqA9=0    #squidA9
SqA10=0   #squidA10
SqA11=0   #squidA11
SqA12=0   #squidA12
SqA13=0   #squidA13
SqA14=0   #squidA14
SqA15=0   #squidA15
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
Sqg10=0   #squidg10
Sqg11=0   #squidg11
Sqg12=0   #squidg12
Sqg13=0   #squidg13
Sqg14=0   #squidg14
Sqg15=0   #squidg15
Sqg16=0   #squidg16
Sqg17=0   #squidg17
#####End variables section#####

#####Start XML labels section#####
#Words to search, it means, the xml labels for squid
label="<filter>"                   #Start label for firewall rules
label1="</filter>"                 #End label for firewall
label2="<aliases>"                 #Start label for aliases
label3="</aliases>"                #End label for aliases
label4="<squidguarddest>"          #Start label for target categories
label5="</squidguarddest>"         #End label for target categories
label6="<squidguardacl>"           #Start label for acl groups
label7="</squidguardacl>"          #End label for acl groups
label8="<nat>"                     #Start label for nats
label9="<onetoone>"                #Start label for one to one nat
label10="</onetoone>"              #End label for one to one nat
label11="<outbound>"               #Start label for outbo8und nat
label12="</outbound>"              #End label for outbound nat
label13="</nat>"                   #End label for nats
labelA="<filter>"                  #Start label for firewall rules
labelA1="</filter>"                #End label for firewall
labelA2="<aliases>"                #Start label for aliases
labelA3="</aliases>"               #End label for aliases
labelA4="<squidguarddest>"         #Start label for target categories
labelA5="</squidguarddest>"        #End label for target categories
labelA6="<squidguardacl>"          #Start label for acl groups
labelA7="</squidguardacl>"         #End label for acl groups
labelA8="<nat>"                    #Start label for nats
labelA9="<onetoone>"               #Start label for one to one nat
labelA10="</onetoone>"             #End label for one to one nat
labelA11="<outbound>"              #Start label for outbo8und nat
labelA12="</outbound>"             #End label for outbound nat
labelA13="</nat>"                  #End label for nats

####SquidGuard Section####
labelsq="<?xml version=\"1.0\"?>"  #Start label for XMLconfiguration file
label1sq="<filter>"                #Start firewall label
label2sq="</filter>"               #Start firewall label
label3sq="<aliases>"               #Start aliases label
label4sq="</aliases>"              #End aliases label
label5sq="<squidguarddest>"        #Start target label
label6sq="</squidguarddest>"       #End target label
label7sq="<squidguardacl>"         #Strat ACL label
label8sq="</squidguardacl>"        #End ACL label
label9sq="<nat>"                   #start nats label
label10sq="<outbound>"             #Start label for outbo8und nat
label11sq="</outbound>"            #End label for outbound nat
label12sq="</pfsense>"             #End label for XML configuration file

####Aux variables for increase the counter####
auxLabel="<separator>"
auxLabel1="</rule>"
#####End XML labels section#####

####Start user section####
#read rhe Xml User file

with open("config.xml") as f:
    for line in f:
        Sq1 += 1
        if label1 in line:
            squid1 = (Sq1)
with open("config.xml") as f:
    for line in f:
        Sq2 += 1
        if auxLabel in line and Sq2 < squid1:
            squid2 = (Sq2-1)
with open("config.xml") as f:
    for line in f:
        Sq3 += 1
        if label2 in line:
            squid3 = (Sq3+1)
with open("config.xml") as f:
    for line in f:
        Sq4 += 1
        if label3 in line:
            squid4 = (Sq4-1)
with open("config.xml") as f:
    for line in f:
        Sq5 += 1
        if label4 in line:
            squid5 = (Sq5+1)
with open("config.xml") as f:
    for line in f:
        Sq6 += 1
        if label5 in line:
            squid6 = (Sq6-1)
with open("config.xml") as f:
    for line in f:
        Sq7 += 1
        if label6 in line:
            squid7 = (Sq7+1)
with open("config.xml") as f:
    for line in f:
        Sq8 += 1
        if label7 in line:
            squid8 = (Sq8-1)
####TEST NATS
with open("config.xml") as f:
    for line in f:
        Sq9 += 1
        if label8 in line:
            squid9 = (Sq9+1)
with open("config.xml") as f:
    for line in f:
        Sq10 += 1
        if label9 in line:
            squid10 = (Sq10)
            with open("config.xml") as f:
                for line in f:
                    Sq11 += 1
                    if auxLabel1 in line and Sq11 == squid10-1 :
                        squid11 = (Sq11)
with open("config.xml") as f:
    for line in f:
        Sq12 += 1
        if auxLabel1 in line and Sq12 == squid11 :
            squid12 = (Sq12)
with open("config.xml") as f:
    for line in f:
        Sq13 += 1
        if label11 in line:
            squid13 = (Sq13-1)
            squid14 = (Sq13+1)
with open("config.xml") as f:
    for line in f:
        Sq14 += 1
        if label12 in line:
            squid15 = (Sq14-1)
####END TEST NATS

#command for cut an interval of speciffic lines and create a new file with those lines
#Firewall rules user doc
command1  = 'sed \''+str(squid1)+','+str(squid2)+' !d\' config.xml > rulesUser.xml'
os.system(command1)
#Aliases user doc
command2  = 'sed \''+str(squid3)+','+str(squid4)+' !d\' config.xml > aliasesUser.xml'
os.system(command2)
#targets user doc
command3  = 'sed \''+str(squid5)+','+str(squid6)+' !d\' config.xml > targetsUser.xml'
os.system(command3)
#ACL user doc
command4  = 'sed \''+str(squid7)+','+str(squid8)+' !d\' config.xml > aclUser.xml'
os.system(command4)
#Nats user doc
command5  = 'sed \''+str(squid9)+','+str(squid11)+' !d\' config.xml > natUser.xml'
os.system(command5)
#One to one user doc
command6  = 'sed \''+str(squid12+1)+','+str(squid13)+' !d\' config.xml > onetooneUser.xml'
os.system(command6)
#Outbound user doc
command7  = 'sed \''+str(squid14)+','+str(squid15)+' !d\' config.xml > outboundUser.xml'
os.system(command7)
####End user section####

####Start the admin section####
#read rhe Xml User file
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
        if auxLabel in line and SqA2 < squidA1:
            squidA2 = (SqA2-1)
with open("conf.xml") as f:
    for line in f:
        SqA3 += 1
        if labelA2 in line:
            squidA3 = (SqA3+1)
with open("conf.xml") as f:
    for line in f:
        SqA4 += 1
        if labelA3 in line:
            squidA4 = (SqA4-1)
with open("conf.xml") as f:
    for line in f:
        SqA5 += 1
        if labelA4 in line:
            squidA5 = (SqA5+1)
with open("conf.xml") as f:
    for line in f:
        SqA6 += 1
        if labelA5 in line:
            squidA6 = (SqA6-1)
with open("conf.xml") as f:
    for line in f:
        SqA7 += 1
        if labelA6 in line:
            squidA7 = (SqA7+1)
with open("conf.xml") as f:
    for line in f:
        SqA8 += 1
        if labelA7 in line:
            squidA8 = (SqA8-1)
####TEST NATS
with open("config.xml") as f:
    for line in f:
        SqA9 += 1
        if labelA8 in line:
            squidA9 = (SqA9+1)
with open("conf.xml") as f:
    for line in f:
        SqA10 += 1
        if labelA9 in line:
            squidA10 = (SqA10)
            with open("conf.xml") as f:
                for line in f:
                    SqA11 += 1
                    if auxLabel1 in line and SqA11 == squidA10-1 :
                        squidA11 = (SqA11)
with open("conf.xml") as f:
    for line in f:
        SqA12 += 1
        if auxLabel1 in line and SqA12 == squidA11 :
            squidA12 = (SqA12)
with open("conf.xml") as f:
    for line in f:
        SqA13 += 1
        if labelA11 in line:
            squidA13 = (SqA13-1)
            squidA14 = (SqA13+1)
with open("conf.xml") as f:
    for line in f:
        SqA14 += 1
        if labelA12 in line:
            squidA15 = (SqA14-1)
####END TEST NATS

#command for cut an interval of speciffic lines and create a new file with those lines
#Firewall rules admin doc
commandA1  = 'sed \''+str(squidA)+','+str(squidA2)+' !d\' conf.xml > rulesAdmin.xml'
os.system(commandA1)
#Aliases admin doc
commandA2  = 'sed \''+str(squidA3)+','+str(squidA4)+' !d\' conf.xml > aliasesAdmin.xml'
os.system(commandA2)
#targets admin doc
commandA3  = 'sed \''+str(squidA5)+','+str(squidA6)+' !d\' conf.xml > targetsAdmin.xml'
os.system(commandA3)
#ACL admin doc
commandA4  = 'sed \''+str(squidA7)+','+str(squidA8)+' !d\' conf.xml > aclAdmin.xml'
os.system(commandA4)
#Nats admin doc
commandA5  = 'sed \''+str(squidA9)+','+str(squidA11)+' !d\' config.xml > natAdmin.xml'
os.system(commandA5)
#One to one admin doc
commandA6  = 'sed \''+str(squidA12+1)+','+str(squidA13)+' !d\' config.xml > onetooneAdmin.xml'
os.system(commandA6)
#Outbound admin doc
commandA7  = 'sed \''+str(squidA14)+','+str(squidA15)+' !d\' config.xml > outboundAdmin.xml'
os.system(commandA7)
####End admin section####

####Start merge Section####
commandMix1 = 'cat rulesUser.xml rulesAdmin.xml > finalRules.xml'
commandremoveU1 = 'rm -r -f rulesUser.xml'
commandremoveA1 = 'rm -r -f rulesAdmin.xml'
os.system(commandMix1)
os.system(commandremoveU1)
os.system(commandremoveA1)
commandMix2 = 'cat aliasesUser.xml aliasesAdmin.xml > finalAliases.xml'
commandremoveU2 = 'rm -r -f aliasesUser.xml'
commandremoveA2 = 'rm -r -f aliasesAdmin.xml'
os.system(commandMix2)
os.system(commandremoveU2)
os.system(commandremoveA2)
commandMix3 = 'cat targetsUser.xml targetsAdmin.xml > finalTargets.xml'
commandremoveU3 = 'rm -r -f targetsUser.xml'
commandremoveA3 = 'rm -r -f targetsAdmin.xml'
os.system(commandMix3)
os.system(commandremoveU3)
os.system(commandremoveA3)
commandMix4='cat aclUser.xml aclAdmin.xml > finalAcl.xml'
commandremoveU4 = 'rm -r -f aclUser.xml'
commandremoveA4 = 'rm -r -f aclAdmin.xml'
os.system(commandMix4)
os.system(commandremoveU4)
os.system(commandremoveA4)
commandMix5='cat natUser.xml natAdmin.xml > finalNat.xml'
commandremoveU5 = 'rm -r -f natUser.xml'
commandremoveA5 = 'rm -r -f natAdmin.xml'
os.system(commandMix5)
os.system(commandremoveU5)
os.system(commandremoveA5)
commandMix6='cat onetooneUser.xml onetooneAdmin.xml > finalOnetoone.xml'
commandremoveU6 = 'rm -r -f onetooneUser.xml'
commandremoveA6 = 'rm -r -f onetooneAdmin.xml'
os.system(commandMix6)
os.system(commandremoveU6)
os.system(commandremoveA6)
commandMix7='cat outboundUser.xml outboundAdmin.xml > finalOutbound.xml'
commandremoveU7 = 'rm -r -f outboundUser.xml'
commandremoveA7 = 'rm -r -f outboundAdmin.xml'
os.system(commandMix7)
os.system(commandremoveU7)
os.system(commandremoveA7)
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
        if auxLabel in line and Sqg3 < squidg2:
            squidg3 = (Sqg3)
with open("config.xml") as f:
    for line in f:
        Sqg4 += 1
        if label3sq in line:
            squidg4 = (Sqg4)
with open("config.xml") as f:
    for line in f:
        Sqg5 += 1
        if label4sq in line:
            squidg5 = (Sqg5)
with open("config.xml") as f:
    for line in f:
        Sqg6 += 1
        if label5sq in line:
            squidg6 = (Sqg6)
with open("config.xml") as f:
    for line in f:
        Sqg7 += 1
        if label6sq in line:
            squidg7 = (Sqg7)
with open("config.xml") as f:
    for line in f:
        Sqg8 += 1
        if label7sq in line:
            squidg8 = (Sqg8)
with open("config.xml") as f:
    for line in f:
        Sqg9 += 1
        if label8sq in line:
            squidg9 = (Sqg9)
with open("config.xml") as f:
    for line in f:
        Sqg10 += 1
        if label9sq in line:
            squidg10 = (Sqg10)
with open("config.xml") as f:
    for line in f:
        Sqg11 += 1
        if label10sq in line:
            squidg11 = (Sqg11)
with open("config.xml") as f:
    for line in f:
        Sqg12 += 1
        if label11sq in line:
            squidg12 = (Sqg12)
with open("config.xml") as f:
    for line in f:
        Sqg13 += 1
        if label12sq in line:
            squidg13 = (Sqg13)


#command for cut an interval of speciffic lines and create a new file with those lines
#before Aliases doc
commandsq1  = 'sed \''+str(squidg)+','+str(squidg1)+' !d\' config.xml > beforeRules.xml'
os.system(commandsq1)
#before Aliases doc
commandsq2  = 'sed \''+str(squidg3)+','+str(squidg4)+' !d\' config.xml > beforeAliases.xml'
os.system(commandsq2)
#before Trgets doc
commandsq3  = 'sed \''+str(squidg5)+','+str(squidg6)+' !d\' config.xml > beforeTargets.xml'
os.system(commandsq3)
#before ACL doc
commandsq4  = 'sed \''+str(squidg7)+','+str(squidg8)+' !d\' config.xml > beforeAcl.xml'
os.system(commandsq4)
#before nat doc
commandsq5  = 'sed \''+str(squidg9)+','+str(squidg10)+' !d\' config.xml > beforeNat.xml'
os.system(commandsq5)
#before outbound doc
commandsq7  = 'sed \''+str(squidg11)+','+str(squidg11)+' !d\' config.xml > beforeOutbound.xml'
os.system(commandsq7)
#before end doc
commandsq8  = 'sed \''+str(squidg12)+','+str(squidg13)+' !d\' config.xml > beforeEnd.xml'
os.system(commandsq8)
#####End get final document section#####

####Start semifinal merge Section####
commandMixsq1 = 'cat beforeRules.xml finalRules.xml > finalsq1.xml'
commandremovesq1 = 'rm -r -f beforeRules.xml'
commandremovesqg1 = 'rm -r -f finalRules.xml'
os.system(commandMixsq1)
os.system(commandremovesq1)
os.system(commandremovesqg1)
commandMixsq2 = 'cat beforeAliases.xml finalAliases.xml > finalsq2.xml'
commandremovesq2 = 'rm -r -f beforeAliases.xml'
commandremovesqg2 = 'rm -r -f finalAliases.xml'
os.system(commandMixsq2)
os.system(commandremovesq2)
os.system(commandremovesqg2)
commandMixsq3 = 'cat beforeTargets.xml finalTargets.xml > finalsq3.xml'
commandremovesq3 = 'rm -r -f beforeTargets.xml'
commandremovesqg3 = 'rm -r -f finalTargets.xml'
os.system(commandMixsq3)
os.system(commandremovesq3)
os.system(commandremovesqg3)
commandMixsq4='cat beforeAcl.xml finalAcl.xml > finalsq4.xml'
commandremovesq4 = 'rm -r -f beforeAcl.xml'
commandremovesqg4 = 'rm -r -f finalAcl.xml'
os.system(commandMixsq4)
os.system(commandremovesq4)
os.system(commandremovesqg4)
commandMixsq5='cat beforeNat.xml finalNat.xml > finalsq5.xml'
commandremovesq5 = 'rm -r -f beforeNat.xml'
commandremovesqg5 = 'rm -r -f finalNat.xml'
os.system(commandMixsq5)
os.system(commandremovesq5)
os.system(commandremovesqg5)
commandMixsq6='cat finalOnetoone.xml > finalsq6.xml'
commandremovesqg6 = 'rm -r -f finalOnetoone.xml'
os.system(commandMixsq6)
os.system(commandremovesqg6)
commandMixsq7='cat beforeOutbound.xml finalOutbound.xml > finalsq7.xml'
commandremovesq7 = 'rm -r -f beforeOutbound.xml'
commandremovesqg7 = 'rm -r -f finalOutbound.xml'
os.system(commandMixsq7)
os.system(commandremovesq7)
os.system(commandremovesqg7)
#####End semifinal merge section#####

#####Start final merge Section#####
commandMixfsq1 = 'cat finalsq1.xml finalsq2.xml > finalmix1.xml'
commandremovefsq1 = 'rm -r -f finalsq1.xml'
commandremovefsqg1 = 'rm -r -f finalsq2.xml'
os.system(commandMixfsq1)
os.system(commandremovefsq1)
os.system(commandremovefsqg1)
commandMixfsq2 = 'cat finalmix1.xml finalsq3.xml > finalmix2.xml'
commandremovefsq2 = 'rm -r -f finalmix1.xml'
commandremovefsqg2 = 'rm -r -f finalsq3.xml'
os.system(commandMixfsq2)
os.system(commandremovefsq2)
os.system(commandremovefsqg2)
commandMixfsq3 = 'cat finalmix2.xml finalsq4.xml > finalmix3.xml'
commandremovefsq3 = 'rm -r -f finalmix2.xml'
commandremovefsqg3 = 'rm -r -f finalsq4.xml'
os.system(commandMixfsq3)
os.system(commandremovefsq3)
os.system(commandremovefsqg3)
commandMixfsq4 = 'cat finalmix3.xml finalsq5.xml > finalmix4.xml'
commandremovefsq4 = 'rm -r -f finalmix3.xml'
commandremovefsqg4 = 'rm -r -f finalsq5.xml'
os.system(commandMixfsq4)
os.system(commandremovefsq4)
os.system(commandremovefsqg4)
commandMixfsq5 = 'cat finalmix4.xml finalsq6.xml > finalmix5.xml'
commandremovefsq5 = 'rm -r -f finalmix4.xml'
commandremovefsqg5 = 'rm -r -f finalsq6.xml'
os.system(commandMixfsq5)
os.system(commandremovefsq5)
os.system(commandremovefsqg5)
commandMixfsq6 = 'cat finalmix5.xml finalsq7.xml > finalmix6.xml'
commandremovefsq6 = 'rm -r -f finalmix5.xml'
commandremovefsqg6 = 'rm -r -f finalsq7.xml'
os.system(commandMixfsq6)
os.system(commandremovefsq6)
os.system(commandremovefsqg6)
commandMixfsq7 = 'cat finalmix6.xml beforeEnd.xml > finalMerge.xml'
commandremovefsq7 = 'rm -r -f finalmix6.xml'
commandremovefsqg7 = 'rm -r -f beforeEnd.xml'
os.system(commandMixfsq7)
os.system(commandremovefsq7)
os.system(commandremovefsqg7)
#####End finalMerge section#####

####Start the final section####
commandfinal1 = 'rm -r -f config.xml'
commandfinal2 = 'rm -r -f conf.xml'
commandfinal3 = 'mv finalMerge.xml config.xml'
os.system(commandfinal1)
os.system(commandfinal2)
os.system(commandfinal3)
####End the final section####
