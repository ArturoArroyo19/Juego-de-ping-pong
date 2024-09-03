#nada que ver xd
elif 50 <= promedio < 69: 
    print(f'Está en zona de recuperación con un promedio de {promedio:.2f}')
else:
    print(f'Ha reprobado con un promedio de {promedio:.2f}')

#Ejercicio 3
while True:
    numero = input("Ingresa el número de 5 dígitos: ")

    if len(numero) == 5 and all('0' <= char <= '9' for char in numero):
        if numero == numero[::-1]: 
            print("El número sí es una capicúa")
        else:
            print("El número no es una capicúa")
        break
    else: 
        print("Ingrese un número válido de 5 dígitos")
numero = input("Ingresa el numero de 5 digitos: ")

#Ejercicio 4
numero_1 = int(input("Ingresa un numero entero: "))
numero_2 = int(input("Ingresa un numero entero: "))
numero_3 = int(input("Ingresa un numero entero: "))
Valido = (numero_1 + numero_2 > numero_3)
if  (numero_1 + numero_2 > numero_3):
    print(f"El triangulo es Valido", Valido)
else:
    print(f"El triangulo no es valido", valido)

#Ejercicio 5
n= int(input("Ingresa un numero entero positivo: "))
for i in range (2,n): 
    if n%i == 0: 
        print("No es primo")
        break
else: 
    print("Es un numero primo")

#Ejercicio 6
ano = int(input("Ingrese un año: "))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    es_bisiesto = True
else:
    es_bisiesto = False
if 2001 <= ano <= 2100:
    es_siglo_xxi = True
else:
    es_siglo_xxi = False
if es_bisiesto:
    print(f"El año {ano} es bisiesto.")
else:
    print(f"El año {ano} no es bisiesto.")

if es_siglo_xxi:
    print(f"El año {ano} pertenece al siglo XXI.")
else:
    print(f"El año {ano} no pertenece al siglo XXI.")


#Ejercicio 7
pin_correcto = "1234"
saldo = 1000
intentos = 0
while intentos < 3:
    pin = input("Ingrese su PIN de 4 dígitos: ")
    if pin == pin_correcto:
        print("PIN correcto. Acceso concedido.")
        break
    else:
        intentos += 1
        print(f"PIN incorrecto. Intentos restantes: {3 - intentos}")
if intentos == 3:
    print("Acceso bloqueado. Por favor, contacte con su banco.")
else:
    while True:
        print("\nOpciones:")
        print("1. Ver saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            print(f"Su saldo es: ${saldo}")

        elif opcion == "2":
            cantidad = int(input("Ingrese la cantidad a retirar: "))
            if cantidad <= saldo:
                saldo -= cantidad
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")
            else:
                print("No tiene suficiente saldo para realizar el retiro.")

        elif opcion == "3":
            cantidad = int(input("Ingrese la cantidad a depositar: "))
            saldo += cantidad
            print(f"Depósito exitoso. Su nuevo saldo es: ${saldo}")

        elif opcion == "4":
            print("Gracias por utilizar nuestro cajero automático.")
            break
        else:
            print("Opción inválida. Por favor, inténtelo de nuevo.")
