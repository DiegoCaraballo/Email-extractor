
#!/usr/bin/python
# -*- coding: utf-8 -*-

from googlesearch import search
import random
import os
import time
import sqlite3
from sqlite3 import Error

# Menú Principal
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
			cantRes = int(input("Cantiad de resultados en Google: ")) 
			extractFraseGoogle(frase, cantRes)
		
		elif (opcion == "3"):
			print ("")
			print ("1 - Seleccionar una frase")
			print ("2 - Todos los correos")
			opcListar = input("Ingrese Opcion: ")
			
			if (opcListar == "1"):
				listarPorFrase()

			elif (opcListar == "2"):
				listarTodo("Emails.db")

		elif (opcion == "4"):
			print ("")
			print ("1 - Guardar una correos de una frase")
			print ("2 - Guardar todos los correos")

		else:			
			print ("Seleccione un opcion correcta")
			time.sleep(2)
			clear()
			menu()
		
	except:
		"Error en funcion Menu"

# Insertar correo, frase y Url en base de datos
def insertEmail(db_file, email, frase, url):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		c.execute("INSERT INTO emails (frase, email, url) VALUES (?,?,?)", (frase, email, url))
		conn.commit()
		conn.close()

	except Error as e:
		print(e)
	finally:
		conn.close()

# Buscar correo en la base de datos
def searchEmail(db_file):
	pass
    #try:
       #conn = sqlite3.connect(db_file)
	#except Error as e:
		#print(e)
	#finally:
		# conn.close()

# Crea tabla principal		
def crearTabla(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		
		#c.execute('drop table if exists emails')

		sql = '''create table if not exists emails 
				(ID INTEGER PRIMARY KEY AUTOINCREMENT,
				 frase varchar(500) NOT NULL,
				 email varchar(200) NOT NULL,
				 url varchar(500) NOT NULL)'''

		c.execute(sql)
		c.close()

	except Error as e:
		print(e)
	finally:
		conn.close()

# Lista correos por frase
def listarPorFrase():
	pass

# Lista todos los correos
def listarTodo(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		c.execute("SELECT * FROM emails")

		for i in c:

			print ("")
			print ("Numero: " + str(i[0]))
			print ("Frase: " + str(i[1]))
			print ("Email: " + str(i[2]))
			print ("Url: " + str(i[3]))
			print ("-------------------------------------------------------------------------------")

		c.close()
		
		print ("")
		input("Presione una tecla para continuar")
		menu()

	except Error as e:
		print(e)
	finally:
		conn.close()

# Extrae los correos de una Url - 2 niveles
def extractUrl(url):
	pass

# Extrae los correos de todas las Url encontradas en las busquedas
# De cada Url extrae los correo - 2 niveles
def extractFraseGoogle(frase, cantRes):

	for url in search(frase, stop=cantRes):
            print(url)

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
insertEmail("Emails.db", "Programadores en Uruguay", "prueba@gmail.com", "www.pythondiario.com")
