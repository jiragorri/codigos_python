mi_lista = []

mi_lista.append(1)

print(mi_lista)

mi_lista.remove(1)

print(mi_lista)

mi_lista.append(1)
mi_lista.append(2)
mi_lista.append(3)
mi_lista.append(4)
mi_lista.append(5)

print(mi_lista)

mi_nueva_lista = [2,1]

mi_nueva_lista = mi_nueva_lista + mi_lista

print(mi_nueva_lista)

mi_nueva_lista.pop(2)

print(mi_nueva_lista)

lista_prueba = []

for i in range(10):
    lista_prueba.append(i)

print(lista_prueba)

lista_prueba = []

for i in range(10):
    lista_prueba.append(int(input("ingrese numeros: ")))
                        
print(lista_prueba)

matriz_prueba = [[],[]]

for i in range(10):
    matriz_prueba[0].append(int(input("ingrese numeros para las filas: ")))
    matriz_prueba[1].append(int(input("ingrese numeros para las columnas: ")))
    
print(matriz_prueba)

for fila in matriz_prueba:
    for columna in fila:
        print(columna)

for i in range(len(matriz_prueba)):
    for j in range(len(matriz_prueba[i])):
        print(matriz_prueba[i][j])


