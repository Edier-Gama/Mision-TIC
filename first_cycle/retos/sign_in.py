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
    datos.append((name, identification, email, coordenadas))


    print("Informacion registrada: ")
    for i in datos:
        print(f" Nombre: {i[0]}")
        print(f" Identificacion: {i[1]}")
        print(f" Correo eléctrónico: {i[2]}")
        print(f" coordenadas: {i[3]}")
    exit()
    
    
 
    

if __name__ == "__main__":
    run()



