def adivinanza():
 import random

 intentos = 0
 numero_aleatorio = random.randint(0, 10)

 print( """
    
      Bienvenido al juego de adivinanzas, tendrás que elegir
      un número entre el 1 y el 10, tu misión es adivinarlo

      ¡Mucha Suerte!
    
    """
 )
 while intentos < 20:
    numero = int(input("Ingresa un numero: "))

    intentos = intentos + 1

    if numero < numero_aleatorio:
        print("¡Estas por debajo!")
    if numero > numero_aleatorio:
        print("¡Te pasaste!")
    if numero < 0:
        print("Estás fuera del intervalo")  
    if numero > 10:
        print("Estás fuera del intervalo")         
    if numero == numero_aleatorio:
        intentos = str(intentos)
        print("¡Adivinaste en " + intentos + " intentos!")
        break
         

def menu ():


 print("""

    1 - Adivinanza
    2 - Cerrar sesión 
    
    """
 )
 contador = 0
 homepage = int(input("Elija una opcion: "))

 if ( homepage == 1):
    adivinanza()

 if (homepage == 2):

    print("Hasta pronto")
    exit()

 while homepage > 2:
    print("Error")
    contador = contador + 1
    error = int(input("Digita una opción correcta: "))  

    if contador > 2:
        print("Error")
        break
        exit()



def run():

 print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

name = "60"
password = "06"
captcha = "6"


user = input(("Ingrese su nombre de usuario: "))

if (user==name):
   
  password_1= input(("Digite su contraseña: "))
  
  if (password_1 == password):
    
    captcha_solution = input(("CAPTCHA:¿Cuál es el resultado de 1 + 5? "))
    if (captcha_solution == captcha):
      menu()  
    else:
      print("Error")
      exit()
  else:
    print("Error")
    exit()

else:
  print("Error")
  exit()

#Fin del programa
if __name__ == "__main__":
  run()