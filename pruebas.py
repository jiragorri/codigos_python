num = int(input("ingrese un número a validar: "))
cont = 1
cont2 = 0
temp = ""
res = 0
while cont < (num+1):
    val = list(str(cont))

    if len(val) >= 2:
        ordenado = True
        for i in range(len(val)-1):
            if int(val[i]) > int(val[i+1]):
                ordenado = False
                break
        if ordenado:
            cont2 = cont
    else:
        res = cont
    cont += 1
if len(val) >= 2:
    print(cont2)
else:
    print(res)


