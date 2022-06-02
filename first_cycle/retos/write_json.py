from asyncore import read
import json
import csv

def run():
    
 registros = []
 nombres = []
 ids = []
 correos = []
 lat = []
 lon = []
 zona = [] 
 cabecera = []
    
 with open("archivo.csv", "r", encoding="utf-8") as archivo:
     
    reader= csv.reader(archivo)
    
    cabecera = next(reader)
          
    for line in reader:
      registros.append(line)
    
    for linea in range(len(registros)):
        nombres.append(registros[linea][0])
        ids.append(registros[linea][1])
        correos.append(registros[linea][2])
        lat.append(registros[linea][3])
        lon.append(registros[linea][4])
        zona.append(registros[linea][5])
        
    for i in nombres:
        datos = [
            
            {
                "Nombre": i,
                "Identificacion": registros[0][1]   
            }
        ]
            
        
        print(datos)
            

if __name__ == "__main__":
    run()    