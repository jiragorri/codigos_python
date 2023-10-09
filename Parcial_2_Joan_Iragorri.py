while True:

    Opc = int(input("Seleccione un ejercicio del 1 al 10, para salir presione 0 \n"))
    if Opc == 0:
        break
    if Opc == 1:
        print("Cree una función llamada hola, que reciba un argumento nombre y que imprima en pantalla Hola, nombre")
        def hola(nom):
            print("Hola,", nom)
        nombre_per = input("cual es su nombre: ")
        hola(nombre_per)
    if Opc == 2:
        print("Escriba una función llamada suma, que reciba dos argumentos a y b y que muestre en pantalla el resultado de sumar a y b")
        def suma(a,b):
            sum = a + b
            return sum
        num1 = int(input("ingrese el primer numero a sumar: "))
        num2 = int(input("ingrese el segundo numero a sumar: "))
        res = suma(num1,num2)
        print("el resultado de la suma es, ", res)
    if Opc == 3:
        print("Crear una funciónque toma un argumento año y devuelve True si el año es un año bisiesto, False si no lo es")
        def anio_bis(anio):
            if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
                print("es anio bisiesto")
            else:
                print("el anio no es bisiesto")
        anio_val = int(input("Ingrese anio para validar si es bisiesto: "))
        anio_bis(anio_val)
    if Opc == 4:
        print("Ejercicio pirámide")
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
    if Opc == 5:
        print("Ejercicio números")
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
print("Has salido del programa")