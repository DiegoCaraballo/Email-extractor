<p align="center">
  <img width="560" height="400" src="https://github.com/DiegoCaraballo/Email-extractor/blob/master/EmailExtractor.PNG">
</p>

# Add Feature: 13-07-2022
- You can save the mailing list in a .csv file

# Fix: 13-09-2019
- Fix - The script was pasted when searching for phrases on Google.
- Add Requirements - pip install -r requirements.txt

# Email Extractor Functions

## English 
- (1) Extract emails from a single URL
- (2) Extract emails from a URL (Two Levels) - Search on the page and all its URLs
- (3) Do a Google search, save the Urls found and search the emails
- (4) Same as option 3 but with a list of keywords (TODO)
- (5) You can list the saved emails
- (6) You can save the mailing list in a .txt file
- (7) You can save the mailing list in a .csv file
- (8) Delete Emails from data base
- (9) Exit

- The emails are stored in a Sqlite database ("Emails.db")

## Español
- (1) Extraer los correos de una única URL
- (2) Extraer los correos de una Url (Dos Niveles) - Busca sobre la página y todas sus URL
- (3) Hacer una busqueda en Google, guardar las Urls encontradas y buscar los correos en dichas Urls
- (4) Igual que la opción 3 pero con una lista de palabras (TODO)
- (5) Listar correos guardados
- (6) Se pueden guardar los correo en un archivo .txt
- (7) Se pueden guardar los correo en un archivo .csv
- (8) Eliminar correos de la base de datos
- (9) Salir

- Todos los correos son guardados en una base de datos Sqlite ("Emails.db")

**Versión:** Python 3.x.

# Required modules - Modulos necesarios

pip install -r requirements.txt

[Extraer correos de paginas web con Python](http://www.pythondiario.com/2018/04/extraer-correos-electronicos-de-paginas.html)

## Docker

Docker and docker-compose are required.

In order to use docker follow below instructions:

### Installation 

1. Get an .env file

```
cp .env.example .env
```

2. Start docker container

```
docker-compose up -d --build
```

### Usage

To execute the script and get the options menu:

```
docker exec -ti email-extractor python EmailExtractor.py
```

To get the sqlite db with al e-mails:

```
docker cp email-extractor:Emails.db .
```

To get the file saved, for instance, as "out":

```
docker cp email-extractor:out.txt .
```
