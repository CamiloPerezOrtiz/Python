#!/bin/sh
host=$(hostname -fs)
ssh-keygen -t rsa
cat /root/.ssh/id_rsa.pub | ssh root@192.168.0.141 'cat >> /root/.ssh/authorized_keys'
