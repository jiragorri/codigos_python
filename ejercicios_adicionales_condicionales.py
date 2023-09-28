while True:

    Opc = int(input("Seleccione un ejercicio del 1 al 13, para salir presione 0 \n"))
    if Opc == 0:
        break

    if Opc == 1:
        print("Determinar si un número es divisible por 5 o 3, o ambos.")
        num = int(input("Ingrese un número: "))
        if num % 3 == 0 and num % 5 == 0:
            print("Divisible por ambos")
        elif num % 3 == 0:
            print("Divisible por 3")
        elif num % 5 == 0:
            print("Divisible por 5")
        else:
            print("No es divisible")
    if Opc == 2:
        print("Verificar si un año es un siglo (multiplo de 100) y si es bisiesto.")
        anio = int(input("Ingrese un año: "))

        if (anio % 4 == 0 or anio % 400 == 0) and anio % 100 == 0:
            print("Anio bisiesto y es un siglo")
        else:
            print("Anio normal")
    if Opc == 3:
        print("Determinar si un número es positivo, negativo o cero, y si es múltiplo de 3.")
        num = int(input("Ingrese un número: "))
        if num > 0 and num % 3 == 0:
            print("numero positivo y multiplo de 3")
        elif num < 0 and num % 3 == 0:
            print("numero negativo y multiplo de 3")
        elif num == 0 and num % 3 == 0:
            print("cero")
        else:
            print("No se encuentra en las opciones anteriores")
    if Opc == 4:
        print("Verificar si un número de teléfono ingresado por el usuario es válido (10 dígitos y sin caracteres especiales.")
        tel = input("ingrese número telefónico: ")
        if len(tel) == 10 and tel.isnumeric():
            print("número correcto")
        else:
            print("número incorrecto")
    if Opc == 5:
        print("Determinar si una palabra es un palíndromo (se lee igual al derecho y al revés")
        palabra = input("ingrese una palabra: ")
        invertida = ""
        for letras in palabra:
            invertida = letras + invertida
        
        if palabra == invertida:
            print("es palindomo")
        else:
            print("no es palindromo")
    if Opc == 6:
        print("Calcular el área de un triángulo si se conocen la base y la altura, o el área de un círculo si se conoce el radio.")
        base = int(input("ingrese la base: "))
        altura = int(input("ingrese la altura: "))
        radio = int(input("ingrese el radio: "))
        sel = int(input("seleccione 1 para area triangulo o 2 para area circulo: "))
        if sel == 1:
            if base != 0 and altura != 0:
                area_triangulo = (base*altura)/2
                print("el area del triángulo es: ",area_triangulo)
            else:
                print("no se puede calcular área")
        elif sel == 2:
            if radio != 0:
                area_circulo = round(3.1416 * (radio**2),2)
                print("el area del círculo es: ",area_circulo)
            else:
                print("no se puede calcular área")
        else:
            print("opción no valida")
    if Opc == 7:
        print("Clasificar una persona según su índice de masa corporal (IMC) en las categorías de peso bajo, normal, sobrepeso u obesidad.")
        val_masa = float(input("Ingrese su peso en kg: "))
        val_altura = float(input("Ingrese su altura en metros: "))
        imc = round(float(val_masa/(val_altura**2)),1)
        if imc < 18.5:
            print("ud se encuentra con bajo peso y su imc es: ", imc)
        elif imc > 18.5 and imc <= 25:
            print("ud se encuentra con Normal y su imc es: ", imc)
        elif imc > 25 and imc <= 30:
            print("ud se encuentra con Sobrepeso y su imc es: ", imc)
        elif imc > 30:
            print("ud se encuentra con Obesidad y su imc es: ", imc)
        else:
            print("Opcion no valida, intente de nuevo")
    if Opc == 8:
        print("Verificar si una contraseña cumple con ciertos criterios de seguridad (longitud mínima, incluye números y caracteres especiales")
        contr = input("ingrese contraseña mínimo de 10 dígitos y caracteres especiales: ")
        cont = 0
        if len(contr) == 10:
            for caracter in contr:
                if not caracter.isalnum() or caracter.isnumeric():
                    cont += 1
            if cont >= 1:
                print("Contraseña Correcta")
            else:
                print("Contraseña incorrecta")
                
        else:
            print("Contraseña incorrecta")
    if Opc == 9:
        print("Calcular la edad en días a partir de la fecha de nacimiento.")
        edad = float(input("ingrese la edad: "))
        edad_dias = edad * 365.25
        print("la edad en días es: ", edad_dias)
    if Opc == 10:
        print("Determinar si un número es un número de Armstrong (un número que es igual a la suma de sus propios dígitos elevados a una potencia).")
        num = input("ingrese un número: ")
        larg_num = len(num)
        tot = 0
        for i in num:
            res = int(i) ** larg_num
            tot = tot + res
        if tot == num:
            print("El número es armstrong")
        else:
            print("el número no es armstrong")
    if Opc == 11:
        print("Clasificar un triángulo según sus ángulos en agudo, rectángulo u obtuso.")
        ang1 = int(input("Ingrese el primer ángulo: "))
        ang2 = int(input("Ingrese el segundo ángulo: "))
        ang3 = int(input("Ingrese el tercer ángulo: "))
        if ang1 == 90 or ang2 == 90 or ang3 == 90:
            print("el triángulo es rectángulo")
        elif ang1 < 90 and ang2 < 90 and ang3 < 90:
            print("el triángulo es agudo")
        elif ang1 > 90 or ang2 > 90 or ang3 > 90:
            print("el triángulo es obtuso")
        else:
            print("no corresponde a ningún triángulo")
    if Opc == 12:
        print("Determinar si un número es un número de Harshad (es divisible por la suma de sus propios dígitos")
        num = input("Ingrese número a validar: ")
        sum = 0
        for i in num:
            sum = sum + int(i)
        if int(num) % sum == 0:
            print("el número es de Harshad")
        else:
            print("el numerno no corresponde a Harshad")
    if Opc == 13:
        print("Verificar si una cadena contiene solo letras o solo números.")
        cadena = input("ingrese cadena de texto: ")
        if cadena.isnumeric():
            print("es una cadena numérica")
        elif cadena.isalpha():
            print("es una cadena de texto")
        else:
            print("no cumple las condiciones dadas")
                       
print("Has salido del programa")