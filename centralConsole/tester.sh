#!/bin/bash
################################################################
# This Code Has Been Developed By Jozic Espinoza AKA HackeMatte#
################################################################
# Start code #
##############
for line in $(cat '/home/hackematte/Desktop/centralConsole/ipaddress.txt'); do
####Start the extract for the user XML configuration files
echo "Extrayendo archivo de configuracion de usuario..."
scp root@$line:/cf/conf/config.xml /home/hackematte/Desktop/centralConsole
mv /home/hackematte/Desktop/centralConsole/config.xml /home/hackematte/Desktop/centralConsole/conf.xml
####Start the extract for the admin XML configuration files
echo "Extrayendo archivo de configuracion de administrador..."
cp /home/hackematte/Desktop/TESTPYTHON/config.xml /home/hackematte/Desktop/centralConsole
#This topic will be contemplated when the final system is created
#cp /cf/conf/config.xml /home/hackematte/Desktop/centralConsole
####Execute python script
echo $line > /home/hackematte/Desktop/centralConsole/pythonip.txt
echo "https://$line/pkg_edit.php?xml=squidguard.xml&id=0" > /home/hackematte/Desktop/centralConsole/python.txt
python /home/hackematte/Desktop/centralConsole/test.py
####Delete the user xml config file drom
echo "Eliminando archivo de configuracion del usuario..."
ssh root@$line 'rm -r -f /cf/conf/config.xml'
echo "Moviendo archivo al servidor remoto..."
scp /home/hackematte/Desktop/centralConsole/config.xml root@$line:/cf/conf/config.xml
echo "Eliminando cache..."
ssh root@$line '/bin/rm -f /tmp/config.cache'
echo "Actualizando politicas de administración..."
python /home/hackematte/Desktop/centralConsole/testing.py
echo "Proceso finalizado para servidor $line ..."
rm -r -f /home/hackematte/Desktop/centralConsole/pythonip.txt
rm -r -f /home/hackematte/Desktop/centralConsole/python.txt
done
