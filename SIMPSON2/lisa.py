import requests
import time
import csv
import string

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


while True :  
  respuesta = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
  datos = respuesta.json()
  quote1: str = datos [0]['quote']
  personaje1 : str = datos[0]['character']
  imagen1 = datos [0]['image']  


#código que pilla quote. charactaer y lo envia a su carpeta y crea el csv.
  if personaje1 != 'Homer Simpson' and personaje1 != 'Lisa Simpson' :
    my_dict = {"quote": quote1,"personaje": personaje1}
    with open('file.csv', 'a') as csvfile: 
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)

  elif personaje1 == 'Homer Simpson':
    my_dict = {"quote": quote1,"personaje": personaje1}
    with open('homer.csv', 'a') as csvfile: 
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)

  elif personaje1 == 'Lisa Simpson':
    my_dict = {"quote": quote1,"personaje": personaje1}
    with open('lisa.csv', 'a') as csvfile: 
      w = csv.DictWriter(csvfile, my_dict.keys())
      w.writerow(my_dict)


      

#sacar imagen del link web viene de google esto tb
  img_data = requests.get(imagen1).content
  with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)



#eliminamos los simbolos
  simbolos = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

 # actualizamos conteo de palabras con el conteo de palabras 
  conteoPalabras = word_count(quote1.translate(str.maketrans('', '',simbolos)),conteoPalabras)

  
#metemos la lista en el csv
  with open('numPalabras.csv', 'w') as csvfile: 
      w = csv.writer(csvfile)
      for key, value in conteoPalabras.items():
        w.writerow([key, value]) 



  time.sleep(3)
