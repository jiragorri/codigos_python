'''La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.
La figura ilustra la regla utilizada por los constructores:

La tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.'''

fig = int(input("ingrese la cantidad de bloques: "))

piso, nivel, sum_nivel = 0,0,0

for i in range(1,fig+1):
    piso += i
    if piso <= fig:
        nivel += 1
        sum_nivel += nivel

if sum_nivel == fig:
    print("la altura de la pirámide es: ", nivel)
else:
    print("la cantidad de bloques no da una pirámide exácta")

