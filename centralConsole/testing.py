#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################
# This Code Has Been Developed By Jozic Espinoza AKA HackeMatte#
################################################################
# Start code #
##############
from selenium import webdriver #### Selenium is the webdriver
####phantomjs is the console browser
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any']) ####ignore the ssl protocol
driver.set_window_size(1120, 550)

f = open('/home/hackematte/Desktop/centralizedConsole/centralConsole/pythonip.txt', 'r') #### Read the file pythonip.txt from specific route
line=f.readline()

driver.get('https://'+(line)) #### Enter at the server
print driver.current_url

#############################
###  Start login process  ###
#############################
text_area = driver.find_element_by_id('usernamefld')  #### Enter the user name
text_area.send_keys("admin")
text_area = driver.find_element_by_id('passwordfld') #### Enter the user password
text_area.send_keys("W@rri0rs15")
python_button = driver.find_elements_by_xpath("//input[@name='login' and @value='Sign In']")[0] #### press the login button
python_button.click()
###############################
###    Stop login process   ###
###############################
f = open('/home/hackematte/Desktop/centralizedConsole/centralConsole/python.txt', 'r') #### Read the file python.txt from specific route
auxLine=f.readline()
driver.get(auxLine)
login = driver.find_element_by_name('submit') #### Press the apply changes button 
login.click()
