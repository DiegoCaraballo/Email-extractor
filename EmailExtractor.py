
#!/usr/bin/python
# -*- coding: utf-8 -*-

#query : query string that we want to search for.
#tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
#lang : lang stands for language.
#num : Number of results we want.
#start : First result to retrieve.
#stop : Last result to retrieve. Use None to keep searching forever.
#pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
#Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

#from google import search
import random
import os
import time
 
# to search
query = "Geeksforgeeks"
p = random.randrange(2,6)
 
#for j in search(query, tld="co.in", num=10, stop=1, pause=p):
#    print(j)


def menu():
	try:
		opcion = input("Ingreso Opcion: ")
		if (opcion == "1"):
			print ("Soy el 1")
		elif (opcion == "2"):
			print ("Soy el 2")
		else:
			print ("Seleccione un opcion correcta")
			time.sleep(2)
			clear()
			menu()
		
	except:
		"Error en funcion Menu"
	
# Limpia la pantalla según el sistema operativo
def clear():
	if os.name == "posix":
		os.system("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system("cls")


# Inicio de Programa
menu()
