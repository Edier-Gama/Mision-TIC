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
         
