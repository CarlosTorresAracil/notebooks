# Paso 1: se importan los distintos paquetes que utlizará el código.

import requests 
import time
import string
import csv
import os

# Paso 2: Código que cuenta las palabras y es capaz de actualizar su conteo. 
# Cógio copiado al 100% de google 
def word_count(str,cuentaPalabras):
    counts = cuentaPalabras
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

# Creamos un diccionario donde se almacenarán
conteoPalabras = dict()



# Paso 3: Creación de la carpeta donde se alamacenarán las subcarpetas de cada personaje que almacemará los csv con las frases de cada perosnaje. 
if not os.path.isdir("CARPETA/"):
    os.mkdir("CARPETA/")

# Paso 4: Elimina los símbolos de las frases para permitir el conteo.
simbolos = str.maketrans("","", string.punctuation)
del simbolos[ord("'")]
   
# Paso 5: Lanzamientos de peticiones a la API de los simpsons. Obteniendo Quote, Character y Image
while True :  
# Asignamos temporalmente a variables las conusltas que hace de la web
  respuesta = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
  datosJson = respuesta.json()
  datos = {"Personaje": datosJson[0]["character"], "Quote": datosJson[0]["quote"]}
  imagen = requests.get(datosJson[0]["image"]).content

# Crea directorios dentro de la carpeta principal. Crea la ruta para crear directorios e introduce la imagen. 
  File = datos["Personaje"].translate(simbolos).replace(" ", "_") + ".png"
  Directorio = "CARPETA/"+datos["Personaje"].translate(simbolos).replace(" ", "_")+"/"
  Ruta = os.path.join(Directorio, File)
  if not os.path.isdir(Directorio):
    os.mkdir(Directorio)
  with open (File, "wb") as f:
    f.write(imagen)
#No me ha funcionado y no he sabido  conseguir que lo introduzca en las carpetas. ****


# Crea el csv que y establece la ruta para meter los datos del api por personaje 
  File2 = datos["Personaje"] +".csv"
  Ruta2 = os.path.join(Directorio, File2)
  with open(Ruta2, 'a') as g: 
      w = csv.DictWriter(g, datos.keys())
      w.writerow(datos)


## Utiliza la función definida en el def y nutre el diccionario que luego lo introduce en la carpeta de cada personaje 
  word_count(datos["Quote"], conteoPalabras)
  with open("CARPETA/conteo.csv", "w") as csvfile:
        Data = ["Quote", "Conteo"]
        Data2 = csv.DictWriter(csvfile, fieldnames=Data)
        Data2.writeheader()
        for Data3 in conteoPalabras:
            Data2.writerow({"Quote": Data3, "Conteo": conteoPalabras[Data3]})

#Establece un timer que ejecuta el while cada x tiempo. 
  time.sleep(30)

