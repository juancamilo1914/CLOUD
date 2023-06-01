peso = float(input("ingese su peso en kilogramos: "))
altura = float(input("ingrese su estatura: "))

IMC =  peso / altura ** 2

print ("su IMC es: ", str(IMC))

if IMC <= 18.15:
	print("por debajo")
elif IMC >= 18.15 or IMC <=  24.9:
		print("saludable")
elif IMC >= 25 or IMC <= 29.9:
		print("sobre peso")
elif IMC >= 30 or IMC <= 34.9:
		print("obesidad_1")
elif IMC >= 35 or IMC <= 39.9:
        print("obesidad_2")
elif IMC >= 40:
    print("obesidd_3")
