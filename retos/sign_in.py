def run():
    
    print("Diligencie los siguientes datos")
    

    name = input("Escriba su nombre: ")
    name = name.upper()
    identification = int(input("Digite su número de identidificación: "))


    cadena = "@ucaldas.edu.co"
    email = input("Escriba su correo eléctronico: ")


    while cadena not in email:
        email = input("Escriba su correo eléctronico nuevamente, verifique que sea con dominio: @ucaldas.edu.co: ")


    latitud = float(input("Ingrese su latitud actual: "))
    longitud = float(input("Ingrese su altitud actual: "))
    coordenadas = "Lat: " + str(latitud) + " Lon: " + str(longitud)


    datos = []
    datos.append([name, identification, email, coordenadas])

        
    datos_finales = [
        {"Nombre:  ": [name]},
        {"Identificación: ": [identification]},
        {"Correo electrónico: ": [email]},
        {"Coordenadas: ": [coordenadas]}
    ]

    for i in datos_finales:
        print("Informacion registrada: ")
        print(i)

    exit()


if __name__ == "__main__":
    run()







        
        



        









if __name__ == "__main__":
    run()