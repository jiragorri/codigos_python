while True:

    Opc = int(input("Seleccione punto de parcial del 1 al 8, para salir presione 0 \n"))
    if Opc == 0:
        break
    if Opc == 1:
        print("Calcular la suma de los números del 1 al 100 usando un bucle for")
        temp = 0
        for i in range (1,101):
            temp = i + temp
        print("El resultado de la suma de los números es: ", temp)
    elif Opc == 2:
        print("Calcular el factorial de un número usando un bucle for")
        num = int(input("inserte el número para calcular facturial: \n"))
        val = 1
        for i in range (1,num+1):
            val = val * i
        print("el factorial del número ",num, "es: ", val)
    elif Opc == 3:
        print("Generar una tabla de multiplicar para un número dado usando un bucle for")
        num_tab = int(input("inserte el número para la tabla de multiplicar: "))
        for i in range(1,11):
            print(num_tab, "x", i, "=", i*num_tab)
    elif Opc == 4:
        print("Imprimir números del 1 al 10 usando un bucle while")
        num_ini = 1
        while num_ini <=10:
            print(num_ini)
            num_ini = num_ini + 1
    elif Opc == 5:
        print("Calcular la suma de los números del 1 al 100 usando un bucle while")
        num_pri = 1
        sum_num = 0
        while num_pri <= 100:
            sum_num = sum_num + num_pri
            num_pri = num_pri + 1
        print("la suma de los números es: ", sum_num)
    elif Opc == 6:
        print("Calcular la secuencia de Fibonacci hasta un límite dado usando un bucle while")
        num_fib = int(input("Ingrese el número a validar la serie: "))
        num_ini_fib = 0
        num_fin_fib = 1
        print(num_ini_fib)
        print(num_fin_fib)
        while num_fib > 0: 
            sum_fib = num_ini_fib + num_fin_fib
            print(sum_fib)
            num_ini_fib = num_fin_fib
            num_fin_fib = sum_fib
            num_fib -=1
    elif Opc == 7:
        print("Calcular el costo de una entrada al cine según la edad.")
        edad = int(input("ingrese su edad: "))
        if edad <= 8:
            valor_entrada = 10000
        elif edad > 8 and edad <= 15:
            valor_entrada = 13000
        elif edad > 15 and edad <= 25:
            valor_entrada = 17000
        elif edad > 25 and edad <= 40:
            valor_entrada = 22000
        else:
            valor_entrada = 25000
        print("el valor de su entrada de acuerdo a su edad que es:", edad, "años, es:", valor_entrada)

    elif Opc == 8:
        print("Calcular el IMC (Índice de Masa Corporal) de una persona y clasificarla.")
        val_masa = float(input("Ingrese su peso en kg: "))
        val_altura = float(input("Ingrese su altura en metros: "))
        imc = round(float(val_masa/(val_altura**2)),1)
        if imc > 18.5 and imc <= 25:
            print("ud se encuentra con Normopeso y su imc es: ", imc)
        elif imc > 25 and imc <= 30:
            print("ud se encuentra con Sobrepeso y su imc es: ", imc)
        elif imc > 30 and imc <= 35:
            print("ud se encuentra con Obesidad Moderada y su imc es: ", imc)
        elif imc > 35 and imc <= 40:
            print("ud se encuentra con Obesidad Grave y su imc es: ", imc)
        elif imc > 40 and imc <= 45:
            print("ud se encuentra con Obesidad Morbida y su imc es: ", imc)
        elif imc > 50:
            print("ud se encuentra con Doble Obesidad Morbida y su imc es: ", imc)
        else:
            print("su imc no se ha podido clasificar, valide los datos ingresados")   
    else:
        print("Opcion no valida, intente de nuevo")

print("Has salido del programa")
