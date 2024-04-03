#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:38:42 2020

@author: aayog
"""

import socket
import pickle

port_number = 5555
server_ip = '127.0.0.1'  # put destination address here

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = pickle.dumps([1,2,3,4,5])
    s.sendto(msg, (server_ip, port_number))
    print("Sent")