import platform
import os
import sys
import socket
import psutil
import time
import shutil

def exo1():
   print(platform.system())
   print(platform.uname())
   print(platform.processor())
   print(platform.version())
   print(platform.platform())
   print(socket.gethostname())
   print(socket.gethostbyname(socket.gethostname()))

def exo2(dir):
   #print(os.listdir(dir))
   files = os.listdir(dir)
   for f in files:
      print(f+" : "+str(os.path.getsize(f))+" octets")

def exo3():
   print(psutil.virtual_memory())

def exo4():
   while True:
      print(psutil.virtual_memory().percent)
      time.sleep(5)

def exo5(path):
   print(shutil.disk_usage(path))

menu = int(input("Entrez un chiffre pour acceder a l exercice (de 1 a 7)\n"))
direc = "/Users/admin/Desktop/python"
#path = "/"
match menu:
   case 1:
      exo1()
   case 2:
      exo2(direc)
   case 3:
      exo3()
   case 4:
      exo4()
   case 5:
      exo5(direc)
   case 6:
      exo6()
   case 7:
      exo7()
