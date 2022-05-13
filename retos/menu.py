def menu ():


 print("""

    1 - Adivinanza
    2 - Cerrar sesión 
    
    """
 )

 homepage = int(input("Elija una opcion: "))

 if ( homepage == 1):

    from adivinanza import adivinanza
    adivinanza()

 elif (homepage == 2):

    print("Hasta pronto")
    exit()

 else: 
    error = int(input("Digita una opción correcta: "))   
    error = homepage
 exit()         


