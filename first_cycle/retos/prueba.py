# import os 
# import csv


# def run():
  
#    registros = []
#    places = []

     
#    with open("archivo.csv", "r", encoding="utf-8") as archivo:
     
#      reader= csv.reader(archivo)
          
#      for line in reader:
#        registros.append(line)  
       
#      for line in range(len(registros)):
#        places.append(registros[line][5])
       
#      norte = places.count("NORTE")
#      sur = places.count("SUR")   
#      occidente = places.count("OCCIDENTE")   
#      oriente = places.count("ORIENTE")
     
#      nombre = input("Hola, por favor digita tu nombre")
#      aviso = print(f"Hola {nombre}, Bienvenido. El archivo analizado retorna lo siguiente: ")
              
     
#      if norte > sur and occidente and oriente:
#        print(f"Hay mas usuarios activos en el NORTE con unTotal: {norte}")
#        print(f"En el sur hay: {sur} en el occidente hay: {occidente}, y en el oriente hay: {oriente}")
       
#      elif sur > norte and occidente and oriente:
#        print(f"Hay mas usuarios activos en el SUR: Total: {sur}")
#        print(f"En el norte hay: {norte} en el occidente hay: {occidente}, y en el oriente hay: {oriente}")
       
#      elif occidente > sur and norte and oriente:
#        print(f"Hay mas usuarios activos en el OCCIDENTE: Total: {occidente}")
#        print(f"En el sur hay: {sur} en el norte hay: {norte}, y en el oriente hay: {oriente}")
       
#      elif oriente > sur and occidente and norte:
#        print(f"Hay mas usuarios activos en el ORIENTE: Total: {oriente}")
#        print(f"En el sur hay: {sur} en el occidente hay: {occidente}, y en el norte hay: {norte}")    
     
 
          
# if __name__ == "__main__":
#     run()
    
    
    
     #  def mayor_norte():
    #    nombre = input("Hola, por favor digita tu nombre: ")
    #    os.system("cls")
    #    print(f"Hola {nombre}, Bienvenido. El archivo analizado retorna lo siguiente: ")
    #    print(f"Hay mas usuarios activos en el NORTE con un total de: {norte}")
    #    print(f"En el sur hay: {sur} en el occidente hay: {occidente}, y en el oriente hay: {oriente}")
       
    #  def mayor_occidente():
    #    nombre = input("Hola, por favor digita tu nombre: ")
    #    os.system("cls")
    #    print(f"Hola {nombre}, Bienvenido. El archivo analizado retorna lo siguiente: ")
    #    print(f"Hay mas usuarios activos en el OCCIDENTE con un total de: {occidente}")
    #    print(f"En el sur hay: {sur} en el norte hay: {norte}, y en el oriente hay: {oriente}")
       
    #  def mayor_oriente():
    #    nombre = input("Hola, por favor digita tu nombre: ")
    #    os.system("cls")
    #    print(f"Hola {nombre}, Bienvenido. El archivo analizado retorna lo siguiente: ")
    #    print(f"Hay mas usuarios activos en el ORIENTE con un total de: {oriente}")
    #    print(f"En el sur hay: {sur} en el occidente hay: {occidente}, y en el norte hay: {norte}")    
         
# import os

# def run():


     
#  def mayor(zona_p, area_p, zona_1, area_1, zona_2, area_2, zona_3, area_3):
  
#       nombre = input("Hola, por favor digita tu nombre: ")
#       os.system("cls")
       
#       print(f"Hola {nombre}, Bienvenido. El archivo analizado retorna lo siguiente: ")
#       print(f"Hay mas usuarios activos en el {zona_p} con un total de: {area_p}")
#       print(f"En el {zona_1} hay: {area_1} en el {zona_2} hay: {area_2}, y en el {zona_3} hay: {area_3}")
 
#  norte = 2
#  sur = 2
#  occidente = 2
#  oriente = 122
        
     
#  if norte > sur and norte > occidente and norte > oriente:
#     mayor("NORTE", norte, "SUR", sur, "OCCIDENTE", occidente, "ORIENTE", oriente)
   
#  elif sur > norte and sur > occidente and sur > oriente:
#     mayor("SUR", sur, "NORTE", norte, "OCCIDENTE", occidente, "ORIENTE", oriente)
      
#  elif occidente > sur and occidente > norte and occidente > oriente:
#     mayor("OCCIDENTE", occidente, "SUR", sur, "NORTE", norte, "ORIENTE", oriente)
    
#  elif oriente > sur and oriente > occidente and oriente > norte:
#     mayor("ORIENTE", oriente, "SUR", sur, "OCCIDENTE", occidente, "NORTE", norte)
       
# if __name__=="__main__":
#   run()                            