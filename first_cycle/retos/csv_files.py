import os 
import csv


def run():
  
   registros = []
   places = []

     
   with open("archivo.csv", "r", encoding="utf-8") as archivo:
     
     reader= csv.reader(archivo)
          
     for line in reader:
       registros.append(line)  
       
     for line in range(len(registros)):
       places.append(registros[line][5])
       
     norte = places.count("NORTE")
     sur = places.count("SUR")   
     occidente = places.count("OCCIDENTE")   
     oriente = places.count("ORIENTE")
     
     nombre = input("Hola, por favor digita tu nombre")
     os.system(cls)
     aviso = print(f"Hola {nombre}, Bienvenido. El archivo analizado retorna lo siguiente: ")
              
     
     if norte > sur and occidente and oriente:
       print(f"Hay mas usuarios activos en el NORTE con unTotal: {norte}")
       print(f"En el sur hay: {sur} en el occidente hay: {occidente}, y en el oriente hay: {oriente}")
       
     elif sur > norte and occidente and oriente:
       print(f"Hay mas usuarios activos en el SUR: Total: {sur}")
       print(f"En el norte hay: {norte} en el occidente hay: {occidente}, y en el oriente hay: {oriente}")
       
     elif occidente > sur and norte and oriente:
       print(f"Hay mas usuarios activos en el OCCIDENTE: Total: {occidente}")
       print(f"En el sur hay: {sur} en el norte hay: {norte}, y en el oriente hay: {oriente}")
       
     elif oriente > sur and occidente and norte:
       print(f"Hay mas usuarios activos en el ORIENTE: Total: {oriente}")
       print(f"En el sur hay: {sur} en el occidente hay: {occidente}, y en el norte hay: {norte}")    
     
 
          
if __name__ == "__main__":
    run()
    
        