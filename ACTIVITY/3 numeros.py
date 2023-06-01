numero1= float(input("ingrese el primer numero: "))
numero2 = float(input("ingrese el segundo numero: "))
numero3 = float(input("ingrese el tercer numero: "))

if numero1 >= numero2 >= numero3:
    print("el numero mayor es: ", + numero1)
elif numero1 <= numero2 >= numero3:
    print("el numero mayor es: ", + numero2)
elif numero1 <= numero2 <= numero3:
    print("el numero mayor es: ", + numero3)