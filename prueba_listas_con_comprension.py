lista = []

for i in range(1,11):
    lista.append(i)

print(lista)

lista = [i for i in range(1,11)]

print(lista)

lista = list(range(1,11))

print(lista)


list_op = [dato*dato for dato in range(1,11) if dato % 2 == 0]

print(list_op)

vegetales = ['apio','brocoli','lechuga']
vegetales_may = [i.upper() for i in vegetales]
print(vegetales_may)

list_num = [2,3,4,5,-1,-7,8,10]

for valor in (x**2 for x in list_num if x%2==0):
    print(valor,end=" ")

cua_par = (x**2 for x in list_num if x % 2 == 0)
print(list(cua_par))

list_num_2 = [-3,5,8,4,1,-6,7,10]

def pares(x):
    return x % 2 == 0

print(list(filter(pares,list_num_2)))
print(list(filter(lambda x:x%2==0,list_num_2)))

valor1 = list(map(lambda x:x**3,list_num_2))
print(valor1)

valor2 = list(map(lambda x:x**3,filter(lambda x:x%2==0,list_num_2)))
print(valor2)