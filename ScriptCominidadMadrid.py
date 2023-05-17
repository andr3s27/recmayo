import requests
from bs4 import BeautifulSoup
import csv

#URL
url = 'https://www.comunidad.madrid/servicios/sede-electronica/servicios-telefonicos-telematicos-comunidad-madrid'

#Realizar la solicitud GET
response = requests.get(url)

#Analiza el HTML
soup = BeautifulSoup(response.text, 'html.parser')

#Buscar la tabla que contiene la informacion
table = soup.find('table', {'border': '1'})

#Abrir un archivo CSV para escribir la informacion
with open('comunidadmadrid.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    #Escribir encabezados csv
    writer.writerow(['Nombre_Departamento', ' Email_Asociado'])


    #Iterar las filas y extraer la informacion
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        nombre = cells.text.strip()
        correo = cells.text.strip()

        #Escribir la informacion en el CSV
        writer.writerow([nombre, correo])
