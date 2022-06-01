#Ingresar 5 paises con su población y luego imprimirlas en pantalla


def run():

    paises = []

    for i in range(5):
        pais = input("Nombre del pais: ")
        poblacion = float(input("Ingrese la poblacion: "))
        paises.append((pais, poblacion))
    print(paises)    

if __name__ == "__main__":
    run()