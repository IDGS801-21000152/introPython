print("Comparación de números")
num1 = int(input("Ingresar número n1: "))
num2 = int(input("Ingresar número n2: "))

if num1 > num2 :
    print("El {} es mayor a {}".format(num1, num2))
else :
    print("El {} es mayor a {}".format(num2, num1))


print("----------------- Pedir una edad -----------------")
edad = int(input("Ingresa tu edad: "))

if edad > 18 :
    print("Eres mayor de edad")
elif edad == 18 :
    print("Suertudote ya puedes tomar :D")
else :
    print("Eres menor de edad")