#Elabora un programa que me muestre en pantalla de forma ordenada de menor a
#mayor dos números ingresados por teclado, por ejemplo si ingreso 5 Y 4 deberá
#mostrar, "los números ingresados  son  5 y 4 y organizados  son  4, 5"

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))

if (n1 > n2):
    print("los numeros ingresados son: ", n1, n2, "y organizados son: ", n2, n1)