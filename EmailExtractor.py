#!/usr/bin/python
# -*- coding: utf-8 -*-
# Comentarios en Español
# Blog: www.pythondiario.com

from googlesearch import search
from socket import timeout
import http
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import URLError, HTTPError
import random
import os
import time
import sqlite3
from sqlite3 import Error
import sys
import re
from fake_useragent import UserAgent
from socket import timeout
from urllib.error import HTTPError, URLError
from datetime import datetime
import csv

imageExt = (".jpeg", ".jpg", ".exif", ".tif", ".tiff", ".gif", ".bmp", ".png", ".ppm",
			".pgm", ".pbm", ".pnm", ".webp", ".hdr", ".heif", ".bat", ".bpg", ".cgm", ".svg")
ua = UserAgent()

count_email_in_phrase = 0

# Menú Principal
def menu():
    	
	global count_email_in_phrase
	count_email_in_phrase = 0

	try:
		clear()
		print('		                  .-"""-.                              ')
		print('		                 / .===. \     ')
		print('		                 \/ 6 6 \/')
		print('		                 ( \___/ )')
		print('		  __________ooo___\_____/______________')
		print('		 /                                     \ ')
		print('		 |            EMAIL EXTRACTOR          |')
		print('		 \__________________________ooo________/')
		print('')
		print(' ------------------------------------------------------------------')
		print("|              ENGLISH             -               ESPAÑOL         | ")
		print(" ------------------------------------------------------------------")
		print("1 - Search only in the entered URL - Buscar solo en la URL ingresada")
		print("2 - Search in a url (Two Levels) - Buscar en una URL(Dos Niveles)")
		print("3 - Search phrase in google - Buscar frase en Google")
		print("4 - Same as option 3 but with a list of keywords")
		print("5 - List emails - Listar correos")
		print("6 - Save emails in .txt file - Guardar correos en archivo .txt")
		print("7 - Save emails in .csv file - Guardar correos en archivo .csv")
		print("8 - Delete Emails from Data Base")
		print("9 - Exit - Salir")
		print("")

		opcion = input("Enter option - Ingrese Opcion: ")
		if (opcion == "1"):
			print("")
			print ("Example URL: http://www.pythondiario.com")
			url = str(input("Enter URL - Ingrese URL: "))
			extractOnlyUrl(url)
			input("Press enter key to continue")
			menu()

		if (opcion == "2"):
			print("")
			print ("Example URL: http://www.pythondiario.com")
			url = str(input("Enter URL - Ingrese URL: "))
			extractUrl(url)
			input("Press enter key to continue")
			menu()

		elif (opcion == "3"):
			print("")
			frase = str(input("Enter a phrase to search - Ingrese una frase a buscar: "))
			print ("***Warning: The amount of results chosen impacts the execution time***")
			print ("*** Advertencia: La cantidad de resultados elejidos impacta el tiempo de ejecucion")
			cantRes = int(input("Number of Google links to explore - Cantiad de resultados en Google: "))
			print ("")
			extractFraseGoogle(frase, cantRes)
			input("Press enter key to continue")
			menu()

		elif (opcion == "4"):
			#extractKeywordsList("KeywordsList.txt")
			print("Developing...")
			input("Press enter key to continue")
			menu()
		
		elif (opcion == "5"):
			print ("")
			print ("1 - Select a phrase - Seleccionar una frase")
			print ("2 - Insert a URL")
			print ("3 - All emails - Todos los correos")
			opcListar = input("Enter option - Ingrese Opcion: ")
			
			if (opcListar == "1"):
				listarPorFrase("Emails.db")

			elif (opcListar == "2"):
				listarPorUrl("Emails.db")

			elif (opcListar == "3"):
				listarTodo("Emails.db")

			else:
				print("Incorrect option, return to the menu...")
				time.sleep(2)
				menu()

		elif (opcion == "6"):
			print("")
			print("1 - Save emails from a phrase - Guardar correos de una frase")
			print("2 - Save emails from a URL - Guardar correos de una URL")
			print("3 - Save all emails - Guardar todos los correos")
			opcGuardar = input("Enter Option - Ingrese Opcion: ")
			
			if(opcGuardar == "1"):
				frase = str(input("Enter phrase: "))
				guardarFrase("Emails.db", frase)
				
			elif(opcGuardar == "2"):
				print("Example URL: http://www.pythondiario.com")
				url = str(input("Insert URL: "))
				guardarUrl("Emails.db", url)
				
			elif(opcGuardar == "3"):
				guardarAll("Emails.db")
				
			else:
				print("Incorrect option, return to the menu...")
				time.sleep(2)
				menu()

		elif (opcion == "7"):
			guardarCsv("Emails.db")

		elif (opcion == "8"):
			print("")
			print("1 - Delete emails from a especific URL")
			print("2 - Delete emails from a especific phrase")
			print("3 - Delete all Emails")
			op = input("Enter option: ")

			if(op == "1"):
				print("Example URL: http://www.pythondiario.com")
				url = str(input("Insert URL: "))
				deleteUrl("Emails.db", url.strip())
			
			elif(op == "2"):
				phrase = str(input("Insert Phrase: "))
				deletePhrase("Emails.db", phrase.strip())

			elif(op == "3"):
				deleteAll("Emails.db")

			else:
				print("Incorrect option, return to the menu...")
				time.sleep(2)
				menu()
		
		elif (opcion == "9"):
			sys.exit(0)

		else:			
			print("")
			print ("Select a correct option - Seleccione un opcion correcta")
			time.sleep(3)
			clear()
			menu()
	
	except KeyboardInterrupt:
		input("Press return to continue")
		menu()

	except Exception as e:
		print (e)
		input("Press enter to continue")
		menu()

# Insertar correo, frase y Url en base de datos
def insertEmail(db_file, email, frase, url):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		c.execute("INSERT INTO emails (phrase, email, url) VALUES (?,?,?)", (frase, email, url))
		conn.commit()
		conn.close()

	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()

	finally:
		conn.close()

# Buscar correo en la base de datos
def searchEmail(db_file, email, frase):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		sql = 'SELECT COUNT(*) FROM emails where email LIKE "%' + str(email) + '%" AND phrase LIKE "%' + str(frase) + '%"'
		result = c.execute(sql).fetchone()
		conn.close()

		return (result[0])

	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()

	finally:
		conn.close()

# Crea tabla principal		
def crearTabla(db_file, delete = False):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		
		if(delete == True):
			c.execute('drop table if exists emails')			

		sql = '''create table if not exists emails 
				(ID INTEGER PRIMARY KEY AUTOINCREMENT,
				 phrase varchar(500) NOT NULL,
				 email varchar(200) NOT NULL,
				 url varchar(500) NOT NULL)'''

		c.execute(sql)
		conn.close()

	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()

	finally:
		conn.close()

# Guardar por URL en un archivo .txt
def guardarUrl(db_file, url):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		sql = 'SELECT COUNT(*) FROM emails WHERE url = "' + url.strip() + '"'
		result = c.execute(sql).fetchone()

		if(result[0] == 0):
			print("There are no emails to erase")
			input("Press enter to continue")
			menu()
			
		else:
			nameFile = str(input("Name of the file: "))
			print("")
			print("Save file, please wait...")
			
			f = open(nameFile.strip() + ".txt", "w")
		
			c.execute('SELECT * FROM emails WHERE url = "' + url.strip() + '"')
			
			count = 0
			
			for i in c:
				count += 1
				f.write("")
				f.write("Number: " + str(count) + '\n')
				f.write("Phrase: " + str(i[1]) + '\n')
				f.write("Email: " + str(i[2]) + '\n')
				f.write("Url: " + str(i[3]) + '\n')
				f.write("-------------------------------------------------------------------------------" + '\n')
				
			f.close()
			
		conn.close()
		input("Press enter to continue")
		menu()
		
	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()
		
	except Exception as o:
		print(o)
		input("Press enter to continue")
		menu()
		
	finally:
		conn.close()

# Guardar por frase en un archivo .txt
def guardarFrase(db_file, frase):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		sql = 'SELECT COUNT(*) FROM emails WHERE phrase = "' + frase.strip() + '"'
		result = c.execute(sql).fetchone()

		if(result[0] == 0):
			print("There are no emails to erase")
			input("Press enter to continue")
			menu()
			
		else:
			nameFile = str(input("Name of the file: "))
			print("")
			print("Save file, please wait...")
			
			f = open(nameFile.strip() + ".txt", "w")
		
			c.execute('SELECT * FROM emails WHERE phrase = "' + frase.strip() + '"')
			
			count = 0
			
			for i in c:
				count += 1
				f.write("")
				f.write("Number: " + str(count) + '\n')
				f.write("Phrase: " + str(i[1]) + '\n')
				f.write("Email: " + str(i[2]) + '\n')
				f.write("Url: " + str(i[3]) + '\n')
				f.write("-------------------------------------------------------------------------------" + '\n')
				
			f.close()
			
		conn.close()
		input("Press enter to continue")
		menu()
			
	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()
		
	except Exception as o:
		print(o)
		input("Press enter to continue")
		menu()
		
	finally:
		conn.close()

# Guardar todos los correos en un archivo .txt
def guardarAll(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		sql = 'SELECT COUNT(*) FROM emails'
		result = c.execute(sql).fetchone()

		if(result[0] == 0):
			print("There are no emails to save")
			input("Press enter to continue")
			menu()
			
		else:
			nameFile = str(input("Name of the file: "))
			print("")
			print("Save file, please wait...")
			
			f = open(nameFile + ".txt", "w")
		
			c.execute('SELECT * FROM emails')
			
			count = 0
			
			for i in c:
				count += 1
				f.write("")
				f.write("Number: " + str(count) + '\n')
				f.write("Phrase: " + str(i[1]) + '\n')
				f.write("Email: " + str(i[2]) + '\n')
				f.write("Url: " + str(i[3]) + '\n')
				f.write("-------------------------------------------------------------------------------" + '\n')
				
			f.close()
			
		conn.close()
		
		input("Press enter to continue")
		menu()
		
	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()
		
	except Exception as o:
		print(o)
		input("Press enter to continue")
		menu()
		
	finally:
		conn.close()

# Borra todos los correos de una URL específica
def deleteUrl(db_file, url):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		sql = 'SELECT COUNT(*) FROM emails WHERE url = ' + '"' + url + '"'
		result = c.execute(sql).fetchone()
		
		if(result[0] == 0):
			print("There are no emails to erase")
			input("Press enter to continue")
			menu()
			
		else:
			option = str(input("Are you sure you want to delete " + str(result[0]) + " emails? Y/N :"))
			
			if(option == "Y" or option == "y"):
				c.execute("DELETE FROM emails WHERE url = " + '"' + url + '"')
				conn.commit()

				print("Emails deleted")
				input("Press enter to continue")
				menu()
				
			elif(option == "N" or option == "n"):
				print("Canceled operation, return to the menu ...")
				time.sleep(2)
				menu()
				
			else:
				print("Select a correct option")
				time.sleep(2)
				deleteUrl(db_file, url)
				
		conn.close()
		
	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()
		
	finally:
		conn.close()

# Borra todos los correos de una Frase específica
def deletePhrase(db_file, phrase):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		sql = 'SELECT COUNT(*) FROM emails WHERE phrase = ' + '"' + phrase + '"'
		result = c.execute(sql).fetchone()
		
		if(result[0] == 0):
			print("There are no emails to erase")
			input("Press enter to continue")
			menu()
			
		else:
			option = str(input("Are you sure you want to delete " + str(result[0]) + " emails? Y/N :"))
			
			if(option == "Y" or option == "y"):
				c.execute("DELETE FROM emails WHERE phrase = " + '"' + phrase + '"')
				conn.commit()

				print("Emails deleted")
				input("Press enter to continue")
				menu()
				
			elif(option == "N" or option == "n"):
				print("Canceled operation, return to the menu ...")
				time.sleep(2)
				menu()
				
			else:
				print("Select a correct option")
				time.sleep(2)
				deleteUrl(db_file, phrase)
				
		conn.close()
				
	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()
		
	finally:
		conn.close()

# Borra todos los correos
def deleteAll(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		sql = 'SELECT COUNT(*) FROM emails'
		result = c.execute(sql).fetchone()

		if(result[0] == 0):
			print("There are no emails to erase")
			input("Press enter to continue")
			menu()
		
		
		else:			
			option = str(input("Are you sure you want to delete " + str(result[0]) + " emails? Y/N :"))
			
			if(option == "Y" or option == "y"):
				c.execute("DELETE FROM emails")
				conn.commit()
				crearTabla("Emails.db", True)
				print("All emails were deleted")
				input("Press enter to continue")
				menu()

			elif(option == "N" or option == "n"):
				print("Canceled operation, return to the menu ...")
				time.sleep(2)
				menu()

			else:
				print("Select a correct option")
				time.sleep(2)
				deleteAll(db_file)
				
		conn.close()

	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()

	finally:
		conn.close()

# Lista correos por frase
def listarPorFrase(db_file):
	try:
		phrase = str(input("Inserter phrase: "))
		conn = sqlite3.connect(db_file)
		c = conn.cursor()
		
		sql = 'SELECT COUNT(*) FROM emails WHERE phrase LIKE "%' + phrase.strip() + '%"'
		result = c.execute(sql).fetchone()

		if(result[0] == 0):
				print("No results for the specified url")
				input("Press enter to continue")
				menu()
				
		else:
			c.execute('SELECT * FROM emails WHERE phrase LIKE "%' + phrase.strip() + '%"')

			for i in c:

				print ("")
				print ("Number: " + str(i[0]))
				print ("Phrase: " + str(i[1]))
				print ("Email: " + str(i[2]))
				print ("Url: " + str(i[3]))
				print ("-------------------------------------------------------------------------------")

		conn.close()
		
		print ("")
		input("Press enter key to continue")
		menu()
		
	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()
	
	finally:
		conn.close()

# Lista correos por URL
def listarPorUrl(db_file):
	try:
		print("Example URL: http://www.pythondiario.com ")
		url = str(input("Insert a Url: "))
		conn = sqlite3.connect(db_file)
		c = conn.cursor()

		sql = 'SELECT COUNT(*) FROM emails WHERE url LIKE "%' + url.strip() + '%"'
		result = c.execute(sql).fetchone()

		if(result[0] == 0):
				print("No results for the specified url")
				input("Press enter to continue")
				menu()

		else:
			c.execute('SELECT * FROM emails WHERE url LIKE "%' + url.strip() + '%"')

			for i in c:

				print ("")
				print ("Number: " + str(i[0]))
				print ("Phrase: " + str(i[1]))
				print ("Email: " + str(i[2]))
				print ("Url: " + str(i[3]))
				print ("-------------------------------------------------------------------------------")

		conn.close()
		
		print ("")
		input("Press enter key to continue")
		menu()

	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()
		
	finally:
		conn.close()

# Lista todos los correos
def listarTodo(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()

		sql = 'SELECT COUNT(*) FROM emails'
		result = c.execute(sql).fetchone()

		if(result[0] == 0):
			print("The data base is Empty")
			input("Press enter to continue")
			menu()

		c.execute("SELECT * FROM emails")

		for i in c:

			print ("")
			print ("Number: " + str(i[0]))
			print ("Phrase: " + str(i[1]))
			print ("Email: " + str(i[2]))
			print ("Url: " + str(i[3]))
			print ("-------------------------------------------------------------------------------")

		conn.close()
		
		print ("")
		input("Press enter key to continue")
		menu()

	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()

	finally:
		conn.close()

# Extrae los correos de una única URL
def extractOnlyUrl(url):
	try:
		print ("Searching emails... please wait")

		count = 0
		listUrl = []

		req = urllib.request.Request(
    			url, 
    			data=None, 
    			headers={
        		'User-Agent': ua.random
    		})

		try:
			conn = urllib.request.urlopen(req, timeout=10)

		except timeout:
			raise ValueError('Timeout ERROR')

		except (HTTPError, URLError):
			raise ValueError('Bad Url...')

		status = conn.getcode()
		contentType = conn.info().get_content_type()

		if(status != 200 or contentType == "audio/mpeg"):
			raise ValueError('Bad Url...')

		html = conn.read().decode(conn.headers.get_content_charset())

		emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}', html)

		for email in emails:
			if (email not in listUrl and not email.endswith(imageExt)):
				count += 1
				print(str(count) + " - " + email)
				listUrl.append(email)
				if(searchEmail("Emails.db", email, "Especific Search") == 0):
					insertEmail("Emails.db", email, "Especific Search", url)

		print("")
		print("***********************")
		print(str(count) + " emails were found")
		print("***********************")

	except KeyboardInterrupt:
		input("Press return to continue")
		menu()

	except Exception as e:
		print (e)
		input("Press enter to continue")
		menu()

# Extrae los correos de una Url - 2 niveles
def extractUrl(url):
	print ("Searching emails... please wait")
	print ("This operation may take several minutes")
	try:
		count = 0
		listUrl = []
		req = urllib.request.Request(
    			url, 
    			data=None, 
    			headers={
        		'User-Agent': ua.random
    		})

		try:
			conn = urllib.request.urlopen(req, timeout=10)

		except timeout:
			raise ValueError('Timeout ERROR')

		except (HTTPError, URLError):
			raise ValueError('Bad Url...')

		status = conn.getcode()
		contentType = conn.info().get_content_type()

		if(status != 200 or contentType == "audio/mpeg"):
			raise ValueError('Bad Url...')

		html = conn.read().decode(conn.headers.get_content_charset())
		
		emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", html)
		print ("Searching in " + url)
		
		for email in emails:
			if (email not in listUrl and not email.endswith(imageExt)):
					count += 1
					print(str(count) + " - " + email)
					listUrl.append(email)
					if(searchEmail("Emails.db", email, "Especific Search") == 0):
						insertEmail("Emails.db", email, "Especific Search", url)

		soup = BeautifulSoup(html, "lxml")
		links = soup.find_all('a')

		print("They will be analyzed " + str(len(links) + 1) + " Urls..." )
		time.sleep(2)

		for tag in links:
			link = tag.get('href', None)
			if link is not None:
				try:
					print ("Searching in " + link)
					if(link[0:4] == 'http'):
						req = urllib.request.Request(
							link, 
							data=None, 
							headers={
							'User-Agent': ua.random
							})

						try:
							f = urllib.request.urlopen(req, timeout=10)

						except timeout:
							print("Bad Url..")
							time.sleep(2)
							pass

						except (HTTPError, URLError):
							print("Bad Url..")
							time.sleep(2)
							pass

						status = f.getcode()
						contentType = f.info().get_content_type()

						if(status != 200 or contentType == "audio/mpeg"):
							print("Bad Url..")
							time.sleep(2)
							pass
						
						s = f.read().decode('utf-8')

						emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", s)

						for email in emails:
							if (email not in listUrl and not email.endswith(imageExt)):
								count += 1
								print(str(count) + " - " + email)
								listUrl.append(email)
								if(searchEmail("Emails.db", email, "Especific Search") == 0):
									insertEmail("Emails.db", email, "Especific Search", url)

				# Sigue si existe algun error
				except Exception:
					pass
		
		print("")
		print("***********************")
		print("Finish: " + str(count) + " emails were found")
		print("***********************")
		input("Press return to continue")
		menu()

	except KeyboardInterrupt:
		input("Press return to continue")
		menu()

	except Exception as e:
		print(e)
		input("Press enter to continue")
		menu()

# Extrae los correos de todas las Url encontradas en las busquedas
# De cada Url extrae los correo - 2 niveles
def extractFraseGoogle(frase, cantRes):
	print ("Searching emails... please wait")
	print ("This operation may take several minutes")
	try:
		listUrl = []
		listEmails = []

		for url in search(frase, stop=cantRes):
			listUrl.append(url)

		for i in listUrl:
			try:
				req = urllib.request.Request(
							i, 
							data=None, 
							headers={
							'User-Agent': ua.random
							})
				try:
					conn = urllib.request.urlopen(req)
				except timeout:
					print("Bad Url..")
					time.sleep(2)
					pass
				except(HTTPError, URLError):
					print("Bad Url..")
					time.sleep(2)
					pass

				status = conn.getcode()
				contentType = conn.info().get_content_type()

				if(status != 200 or contentType == "audio/mpeg"):
					print("Bad Url..")
					time.sleep(2)
					pass

				html = conn.read()

				soup = BeautifulSoup(html, "lxml")
				links = soup.find_all('a')

				print("They will be analyzed " + str(len(links) + 1) + " Urls..." )
				time.sleep(2)

				for tag in links:
					link = tag.get('href', None)
					if link is not None:
    					# Fix TimeOut
						searchSpecificLink(link, listEmails, frase)
		
			except urllib.error.URLError as e:
				print("Problems with the url:" + i)
				print(e)
				pass
			except (http.client.IncompleteRead) as e:
				print(e)
				pass
			except Exception as e:
				print(e)
				pass
		
		print("")
		print("*******")
		print("Finish")
		print("*******")
		input("Press return to continue")
		menu()

	except KeyboardInterrupt:
		input("Press return to continue")
		menu()

	except Exception as e:
		print(e)
		input("Press enter to continue")
		menu()
		
# Extraer lista de palabras claves de txt
def extractKeywordsList(txtFile):
	f = open(txtFile, 'r')
	text = f.read()
	keywordList = text.split(sep='\n')
	for key in keywordList:
    		print(key)

# Limpia la pantalla según el sistema operativo
def clear():
	try:
		if os.name == "posix":
			os.system("clear")
		elif os.name == "ce" or os.name == "nt" or os.name == "dos":
			os.system("cls")
	except Exception as e:
		print(e)
		input("Press enter to continue")
		menu()
   
def searchSpecificLink(link, listEmails, frase):
	try:

		global count_email_in_phrase

		print("Searching in " + link)
		if(link[0:4] == 'http'):
			f = urllib.request.urlopen(link, timeout=10)
			s = f.read().decode('utf-8')
			emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", s)
			for email in emails:
				if (email not in listEmails and not email.endswith(imageExt)):
					count_email_in_phrase += 1
					listEmails.append(email)
					print(str(count_email_in_phrase) + " - " + email)										
					if (searchEmail("Emails.db", email, frase) == 0):
						insertEmail("Emails.db", email, frase, link)
						
	# Sigue si existe algun error	
	except (HTTPError, URLError) as e:
		print(e)
		pass
	except timeout:
		print('socket timed out - URL %s', link)
		pass
	except (http.client.IncompleteRead) as e:
		print(e)
		pass
	except Exception as e:
		print(e)
		pass

def guardarCsv(db_file):
	try:
		conn = sqlite3.connect(db_file)
		c = conn.cursor()

		nameFile = datetime.now().strftime('csvemails_%Y_%m_%d_%H_%M_%S.csv')
		print("")
		print("Creating csv, please wait...")
		
		f = open(nameFile, "w", newline="")
		writer = csv.writer(f)

		header = ['Phrase', 'Email', 'Url']
		writer.writerow(header)
	
		c.execute('SELECT * FROM emails')
				
		for i in c:
			row = [str(i[1]), str(i[2]), str(i[3])]
			writer.writerow(row)
			
		f.close()
			
		conn.close()
		
		input("Press enter to continue")
		menu()
		
	except Error as e:
		print(e)
		input("Press enter to continue")
		menu()
		
	except Exception as o:
		print(o)
		input("Press enter to continue")
		menu()
		
	finally:
		conn.close()

# Inicio de Programa
def Main():
	clear()
	crearTabla("Emails.db", False)	
	menu()

Main()
