import requests
import time
import csv

while True :  
  respuesta = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
  datos = respuesta.json()
  quote1: str = datos [0]['quote']
  personaje1 : str = datos[0]['character']
    
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
    
  time.sleep(15)
  

