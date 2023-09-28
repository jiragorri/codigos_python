#creo el diccionario

usuarios ={
    "Nombre" : [],
    "Apellido" : []
}

#ingreso datos

for i in range(2):
    nombre = input("ingrese el nombre de la persona: ")
    apellido = input("ingrese el apellido de la persona: ")

    usuarios["Nombre"].append(nombre)
    usuarios["Apellido"].append(apellido)

#imprimiendo resultados

for i in range(2):
    print("nombre:", usuarios["Nombre"][i])
    print("apellido:", usuarios["Apellido"][i])

for i in usuarios.keys():
    print(i, end=' ')

for i in usuarios.values():
    print(i, end=' ')

print(list(usuarios.keys()))
print(list(usuarios.values()))
print(list(usuarios.items()))