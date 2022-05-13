import random
def adivinanza():

    print( """
    
      Bienvenido al juego de adivinanzas, tendras que elegir
      un numero entre el 1 y el 10, tu misión es adivinarlo

      ¡Mucha Suerte!
    
    """

    )

random_number = random.randint(0, 10)

def intentos():
 numero = int(input("Ingresa un número al azar: "))

 if numero == random_number:
    print("Adivinaste en x intentos")
 elif numero < random_number:
    print("“!Estas por debajo¡")
 elif numero > random_number:
    print("!Te pasaste¡")

 while not numero == random_number:
    intentos()