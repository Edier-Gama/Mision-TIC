import os 
import csv


def run():
  
   cabecera = []
   registros = []
   places = []
   orientaciones = {}

     
   with open("archivo.csv", "r", encoding="utf-8") as archivo:
     
     reader= csv.reader(archivo)
     
     header = next(reader)
     
     for line in reader:
       registros.append(line)  
       
     for line in range(len(registros)):
       places.append(registros[line][5])
       
       
  
      
       


    
     

       
        
     
                       
if __name__ == "__main__":
    run()
    
        