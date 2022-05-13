def menu ():


 print("""

    1 - Adivinanza
    2 - Cerrar sesión 
    
    """
 )
 contador = 0
 homepage = int(input("Elija una opcion: "))

 if ( homepage == 1):

    from adivinanza import adivinanza
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
       


