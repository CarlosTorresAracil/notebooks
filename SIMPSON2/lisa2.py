import requests
import time
import csv
import string
import os
import shutil
import errno

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
# ya tenemos una variable que almacena en el diccionario los counts
# variable donde almacenamos y comparamos
personajes = []

while True :  
  respuesta = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
  datos = respuesta.json()
  quote1: str = datos [0]['quote']
  personaje1 : str = datos[0]['character']
  imagen1 = datos [0]['image']  




#eliminamos los simbolos
  simbolos = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
# actualizamos conteo de palabras con el conteo de palabras 
  conteoPalabras = word_count(quote1.translate(str.maketrans('', '',simbolos)),conteoPalabras)
  
#metemos la lista en el csv
  with open('NumPalabra/numPalabra.csv', 'w') as csvfile: 
      w = csv.writer(csvfile)
      for key, value in conteoPalabras.items():
        w.writerow([key, value]) 
        
# revisamos si eixte ya se ha creado antes o no
  if personaje1 in personajes:
#opción 1 - como esta dentro ya le mandamos a la carpeta del personaje existente
        ruta = '_'
        carpeta_2 = personaje1
        path2 = os.path.join(ruta,carpeta_2)
        personaje2 = personaje1 + '.csv'
        path3 = os.path.join(path2,personaje2)
#carpeta encontrada envio la frase ahí
        with open(path3,"a") as csvfile:
         csvfile.write("\n")
         csvfile.write(quote1)

  else:
#opcion 2 - como el personaje no esta creado se crea
        personajes.append(personaje1)
        carpeta_1 = personaje1
        parent_dir = '_'
        path = os.path.join(parent_dir,carpeta_1)
        os.mkdir(path)
#introduco mi quote dentro del personaje y hecho esto con la función shutil la meto en mi archivo
        personaje2 = personaje1 + '.csv'
        my_dict = {'quote': quote1} 
        with open(personaje2, 'a') as csvfile:
            w = csv.DictWriter(csvfile, my_dict.keys())
            w.writerow(my_dict)
        shutil.move(personaje2, path)


#sacar imagen del link web viene de google esto tb
        imagen = personaje1 +'.png'
        img_data = requests.get(imagen1).content
        with open('image_name.jpg', 'wb') as handler:
          handler.write(img_data)
        shutil.move(imagen, path)



    
# lanza a al api y pesca cada 30s
  time.sleep(30)




