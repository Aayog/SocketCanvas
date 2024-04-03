#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:38:42 2020

@author: aayog
"""

import socket
import pickle

port = 5555
server_ip = '0.0.0.0' 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind( (server_ip, port) )

while True:
  (msg, addr) = s.recvfrom(1024)
  try:
      array =pickle.loads(msg)
      print(array)
      
  except:
    continue