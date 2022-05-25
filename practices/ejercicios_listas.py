from re import X


def run():

    materia_1 = input("Ingrese una materia: ")
    materia_2 = input("Ingrese una materia: ")
    materia_3 = input("Ingrese una materia: ")
    materia_4 = input("Ingrese una materia: ")
    materia_5 = input("Ingrese una materia: ")

    lista_materias = []

    lista_materias.extend([materia_1, materia_2, materia_3, materia_4, materia_5]) 

    # print(lista_materias)

    for materia in lista_materias:
        nota = input("Que nota sacaste en: ", materia)
        notas = []
        notas.append([nota])

    for n in notas:
        print("En ", materia, " sacaste ", n)



 



if __name__=="__main__":
    run()