#Para agregar 1 elemento a una lista en una posicion exacta, debemos usar:

# lista.insert(1, "")

#Ejemplo .


list_nums = [1,3,4,5]
list_nums = list((1,2,3,4))

list_nums.insert(1, 2)
print(list_nums)

#Esta lista va a insertar antes del 3 el numero 2

#Este nos quita o el ultimo elemento en la lista o el elemento indicado

list_nums.pop(3)
print(list_nums)


#Para organizar una lista por orden alfabético debemos usar eel metodo .sort

list_nums.sort()

# si queremos que se ordene en orden contrario usamos dentro de los parentesis
# la palabra reverse = true

list_nums.sort(reverse = True)

# para saber el index de un elemento usamos el metodo .index("elemento")

list_nums.index(3)

#Para contar cuantos elementos de un cierto tipo hay en nuestra lista debemos
#usar el método .count("valor")

list_nums.count(2)


super_list = [
         {"Firstname": "Edier", "Lastname": "Gama"},
         {"Firstname": "Luis", "Lastname": "Torres"},
         {"Firstname": "Luisa", "Lastname": "Fajardo"},
         {"Firstname": "Juan", "Lastname": "Calderon"},
         {"Firstname": "Camila", "Lastname": "Gama"}
]

#-------------------------------tuplas---------------------------------#

tupla = (1,2,3)
meses = ("Enero","Febrero","Marzo")

#Para crearlas con la etiqueta tuple()

tuple_2 = tuple((1,2,3))

#Para eliminar una tupla debo usar (del)

del(tuple_2)
