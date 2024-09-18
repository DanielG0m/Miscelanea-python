import os

titulo="""
Miscelanea de ejercicios
"""
valorHora: 5000

menu = "1. Hallar la superficie de un cuadro \n2. Suma y multiplicacion de numeros \n3. Compra de productos \n4. Suma y multiplicacion de multiples mumeros \n5. Suma y promedio de numeros \n6. Horas trabajadas \n7. Impuestos \n8. Numero mayor \n9. Suma y resta o multiplicacion y division "

while True:
    print(titulo)
    print(menu)
    op = int(input(">. "))

    match op:
        case 1:
            lado = int(input("Ingrese un lado del cuadrado: "))
            print(f"El area del cuadrado es {lado * lado} cm²")
            print(f"El perimetro del cuadrado es {lado * 4} cm")
            os.system('pause')
            os.system('cls')

        case 2:
            x = int(input("Ingrese un numero: "))
            y = int(input("Ingrese un segundo numero: "))
            print(f"La suma de estos numeros es {x+y} \nLa multiplicacion de estos numeros es {x*y}")
            os.system('pause')
            os.system('cls')

        case 3:
            precio = int(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantdad que va a llevar: "))
            print(f"El valor a pagar es: ${precio*cantidad}")
            os.system('pause')
            os.system('cls')

        case 4:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            c = int(input("Ingrese el tercer numero: "))
            d = int(input("Ingrese el cuarto numero: "))
            print(f"La suma de los dos primeros numeros es: {a+b} \n la multiplicacion del tecer y cuarto numero es: {c*d}")
            os.system('pause')
            os.system('cls')

        case 5:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            c = int(input("Ingrese el tercer numero: "))
            d = int(input("Ingrese el cuarto numero: "))
            print(f"La suma de sus de todos los numeros es {a+b+c+d} \n y el promedio de estos es {(a+b+c+d) / 4}")
            os.system('pause')
            os.system('cls')

        case 6:
            horasTrabajada = int(input("Cuantas horas trabajo: "))
            print(f"Su sueldo mensual es: {horasTrabajada*valorHora}")
            os.system('pause')
            os.system('cls')

        case 7:
            salario = int(input("Ingrese su sueldo en dolares: "))
            if salario < 3000:
                print("No debe abonar impuestos")
            else:
                print("Usted debe abonar impuestos")
            os.system('pause')
            os.system('cls')

        case 8:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            if a>b:
                print(f"{a} es el mayor de los dos")
            else:
                print(f"{b} es mayor de los dos")

        case 9:
            a = int(input("Ingrese el primer numero: "))
            b = int(input("Ingrese el segundo numero: "))
            if a>b:
                print(f"su suma es {a+b} \nsu resta es {a-b}")
            else:
                try:
                    print(a/b)
                except ZeroDivisionError:
                    print("no se puede dividir en cero")

                print(f"El producto de ambos es: {a*b}")
                
            os.system('pause')
            os.system('cls')

        case ValueError:
            print("Ingrese un valor valido")
            os.system('pause')
            os.system('cls')