from traceback import print_tb


def run():
    
#  numeros = [i * 2 for i in range(1, 6)]  
#  print(numeros)
   
   # my_list = [1,2,3,4,5]

   # odd = list(map(lambda x: x**2, my_list))

   # print(odd)

   def addprefijo(prefijo):
      return lambda nombre: f'Hola {prefijo}, {nombre}'


   addMr = addprefijo("Mister")
   addSr = addprefijo("Señor")  
   addMiss = addprefijo("Miss")

   print(addMr("Edier")) 
   print(addSr("Gama")) 
   print(addMiss("Laura")) 



if __name__=="__main__":
    run()