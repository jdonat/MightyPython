#!/usr/bin/env python3
import threading 
def compteur(nomThread):
	for i in range(3):
		print(nomThread + " : " + str(i))
threadA = threading.Thread(None, compteur, None, ("Thread A",), {}) 
threadB = threading.Thread(None, compteur, None, ("Thread B",), {}) 
threadA.start() 
threadB.start()