
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

import googlesearch
import random
import os
import time
import sqlite3
from sqlite3 import Error
 
# to search
query = "Geeksforgeeks"
p = random.randrange(2,6)
 
#for j in search(query, tld="co.in", num=10, stop=1, pause=p):
#    print(j)


def menu():
	try:
		clear()
		print ("###################################################################")
		print ("#                                                                 #")
		print ("#                       EMAIL EXTRACTOR                           #")
		print ("#                                                                 #")
		print ("###################################################################")
		print ("")
		print ("1 - Buscar en una URL")
		print ("2 - Buscar palabra en Google")
		print ("3 - Listar correos")
		print ("4 - Guardar correos en archivo .txt")
		print ("")

		opcion = input("Ingrese Opcion: ")
		if (opcion == "1"):
			url = str(input("Ingrese URL: "))
			searchEmail("Emails.db")
			extractUrl(url)

		elif (opcion == "2"):
			frase = str(input("Ingrese una frase a buscar: "))
			print ("*** Advertencia: La cantidad de resultados elejidos impacta el tiempo de ejecucion")
			cantRes = input("Cantiad de resultados en Google: ") 
			extractFraseGoogle(frase, cantRes)
		
		elif (opcion == "3"):
			print ("")
			print ("1 - Seleccionar una categoria")
			print ("2 - Todos los correos")
			opcListar = input("Ingrese Opcion: ")
			
			if (opcListar == "1"):
				listarPorCategoria()

			elif (opcListar == "2"):
				listarTodo()

		elif (opcion == "4"):
			print ("")
			print ("1 - Guardar una categoria")
			print ("2 - Guardar todos los correos")

		else:			
			print ("Seleccione un opcion correcta")
			time.sleep(2)
			clear()
			menu()
		
	except:
		"Error en funcion Menu"

# Insertar correo, categoria y Url en base de datos
def insertEmail(db_file, email, categoria, url):
	pass

# Buscar correo en la base de datos
def searchEmail(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

def crearTabla(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		sql = '''create table if not exists emails 
				(id int integer primary key,
				 categoria varchar(500) NOT NULL,
				 email varchar(200) NOT NULL)'''

		c.execute(sql)
		c.close()

	except Error as e:
		print(e)
	finally:
		conn.close()

def listarPorCategoria():
	pass

def listarTodo():
	pass

# Extrae los correos de una Url - 2 niveles
def extractUrl(url):
	pass

# Extrae los correos de todas las Url encontradas en las busquedas
# De cada Url extrae los correo - 2 niveles
def extractFraseGoogle(frase, cantRes):
	pass

# Limpia la pantalla según el sistema operativo
def clear():
	try:
		if os.name == "posix":
			os.system("clear")
		elif os.name == "ce" or os.name == "nt" or os.name == "dos":
			os.system("cls")
	except:
		"Error al borrar pantalla"


# Inicio de Programa
clear()
crearTabla("Emails.db")	
menu()
