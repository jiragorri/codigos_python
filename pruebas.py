'''cont = 1
cont_prim = 0
num = int(input("ingrese un numero: "))

while num >= cont:
    if num % cont == 0:
        cont_prim += 1
    print(cont_prim)
    cont += 1

if cont_prim > 2:
    print("el numero",num,"no es primo")
else:
    print("el numero",num,"numero primo")'''

print("Imprimir los primeros 10 números primos usando un bucle while")
cant_prim = 0
num = 1        
while cant_prim < 10:
    
    cont = 1
    cont_prim = 0

    while num >= cont:
        if num % cont == 0:
            cont_prim += 1
        cont += 1
    
    if cont_prim <= 2:
        print(num)
        cant_prim +=1
    
    num += 1
