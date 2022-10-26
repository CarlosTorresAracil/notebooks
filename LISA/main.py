import requests 
import time
import string
import csv
import os

# cuenta las palabras y las mete en un diccionario 
# sacado de goole 
def word_count(str,cuentaPalabras):
    counts = cuentaPalabras
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
conteoPalabras = dict()



# indica que el directorio donde se trabajará es CARPETA
if not os.path.isdir("CARPETA/"):
    os.mkdir("CARPETA/")

#eliminamos los simbolos
simbolos = str.maketrans("","", string.punctuation)
del simbolos[ord("'")]
   
    
while True :  
# definimos lo que pesca de la web de simpsons
  respuesta = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
  datosJson = respuesta.json()
  datos = {"Personaje": datosJson[0]["character"], "Quote": datosJson[0]["quote"]}
  imagen = requests.get(datosJson[0]["image"]).content

# crea la ruta oara crear directorios e introduce la imagen
  File = datos["Personaje"].translate(simbolos).replace(" ", "_") + ".png"
  Directorio = "CARPETA/"+datos["Personaje"].translate(simbolos).replace(" ", "_")+"/"
  Ruta = os.path.join(Directorio, File)
  if not os.path.isdir(Directorio):
    os.mkdir(Directorio)
  with open (File, "wb") as f:
    f.write(imagen)

# creamos la ruta de archivos csv por personaje 
  File2 = datos["Personaje"] +".csv"
  Ruta2 = os.path.join(Directorio, File2)
  with open(Ruta2, 'a') as g: 
      w = csv.DictWriter(g, datos.keys())
      w.writerow(datos)


## tira del def y nutre el diccionario 
  word_count(datos["Quote"], conteoPalabras)
  with open("CARPETA/conteo.csv", "w") as csvfile:
        Data = ["Quote", "Conteo"]
        Data2 = csv.DictWriter(csvfile, fieldnames=Data)
        Data2.writeheader()
        for Data3 in conteoPalabras:
            Data2.writerow({"Quote": Data3, "Conteo": conteoPalabras[Data3]})


  time.sleep(5)

