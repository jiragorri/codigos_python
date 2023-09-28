while True:

    Opc = int(input("Seleccione un ejercicio del 1 al 10, para salir presione 0 \n"))
    if Opc == 0:
        break
    if Opc == 1:
        print("Calcular la suma de los números pares del 1 al 50.")
        sum = 0    
        for i in range(1,51):
            if i % 2 == 0:
                sum = sum + i
        print("la suma de los números es: ", sum)
    elif Opc == 2:
        print("Imprimir los números del 10 al 1 en orden descendente usando un bucle while.")
        num = 10
        while num > 0:
            print(num)
            num -= 1
    elif Opc == 3:
        print("Calcular el producto de los primeros 10 números naturales usando un bucle for")
        multi = 1
        for i in range(1,11):
            multi = multi * i
        print("el resultado de la multiplicación es: ", multi)
    elif Opc == 4:
        print("Imprimir los números del 1 al 100 que son divisibles por 7")
        for i in range(1,101):
            if i % 7 == 0:
                print(i)
    elif Opc == 5:
        print("Generar la secuencia de Fibonacci hasta el término número 20 usando un bucle for.")
        num_ini_fib = 0
        num_fin_fib = 1
        print(num_ini_fib)
        print(num_fin_fib)
        for i in range (18): 
            sum_fib = num_ini_fib + num_fin_fib
            print(sum_fib)
            num_ini_fib = num_fin_fib
            num_fin_fib = sum_fib
    elif Opc == 6:
        print("Calcular el promedio de una lista de números ingresados por el usuario usando un bucle while")
        cant_num = int(input("ingrese la cantidad de numeros a promediar: "))
        cont = 0
        sum = 0
        prom = 0
        while cant_num > 0:
            num_ing = int(input("Ingrese un número: "))
            sum = sum + num_ing
            cont += 1
            cant_num -= 1
        prom = sum/cont
        #prome = sum + cont
        print("el promedio de los numeros es: ", prom)
    elif Opc == 7:
        print("Imprimir los primeros 10 números primos usando un bucle while")
        cant_prim = 0
        num_prim = 1        
        while cant_prim < 10:

            cont_cil = 1
            cont_prim = 0

            while num_prim >= cont_cil:
                if num_prim % cont_cil == 0:
                    cont_prim += 1
                cont_cil += 1
    
            if cont_prim <= 2:
                print(num_prim)
                cant_prim +=1
    
            num_prim += 1
    elif Opc == 8:
        print("Imprimir los caracteres de una cadena en mayúsculas y minúsculas usando un bucle for")
        cadena = input("Introducir la palabra: ")
        for caracter in cadena:
            new_cadena = cadena.upper()
            print(caracter)
        print(new_cadena)

        for caracter in cadena:
            new_cadena = cadena.lower()
            print(caracter)
        print(new_cadena)
    elif Opc == 9:
        print("Calcular el factorial de un número ingresado por el usuario usando un bucle for.")
        num = int(input("inserte el número para calcular facturial: \n"))
        val = 1
        for i in range (1,num+1):
            val = val * i
        print("el factorial del número ",num, "es: ", val)
    elif Opc == 10:
        print("Imprimir los cuadrados de los números del 1 al 10 usando un bucle for.")
        for i in range(1,11):
            print(i, "^", 2, "=", i**2)

print("Has salido del programa")