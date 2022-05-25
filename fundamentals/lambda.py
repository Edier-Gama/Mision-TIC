def run():
    
#  numeros = [i * 2 for i in range(1, 6)]  
#  print(numeros)
   
   my_list = [1,2,3,4,5]

   odd = list(map(lambda x: x**2, my_list))

   print(odd)

if __name__=="__main__":
    run()