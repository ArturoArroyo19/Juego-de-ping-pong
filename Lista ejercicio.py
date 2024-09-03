#Ejercicio 1 - Dada una lista de palabras, cuenta cuántas veces aparece la palabra "Python" en la lista
palabra = ["Python", "Java", "C++", "Python", "JavaScript", "Python", "C#"]
Contador = 0
Python = "Python"
for palabra in palabra:
    if palabra in Python:
        Contador += 1
print("La cantidad de veces que se repite la palabra python son", Contador, "veces")

#Ejercico 2
def convertir_lista_a_mayusculas(lista):
    def convertir_mayusculas(cadena):
        resultado = ""
        for caracter in cadena:
            if 'a' <= caracter <= 'z':
                resultado += chr(ord(caracter) - 32)
            else:
                resultado += caracter
        return resultado

    return [convertir_mayusculas(cadena) for cadena in lista]

frases = ["hola", "mundo", "python", "es", "genial"]
frases_mayusculas = convertir_lista_a_mayusculas(frases)
print(frases_mayusculas)
#Ejercicio 3
palabras = ["sol", "luna", "cielo", "mar", "estrella", "pez"]
palabras_filtradas = [palabra for palabra in palabras if len(palabra) >= 4]
print(palabras_filtradas) 

#Ejercico 4
def encontrar_maximo(lista):
    maximo = lista[0]  
    for numero in lista:
        if numero > maximo:
            maximo = numero  
    return maximo

numeros = [15, 22, 8, 34, 9, 6, 17]
maximo = encontrar_maximo(numeros)
print(maximo)  

#Ejercicio 5
numero = [-3, 5, -7, 2, -8, 10, -4, 6]
def contar_positivos(numeros):
    positivos = len([num for num in numeros if num > 0])
    return positivos
cantidad_positivos = contar_positivos(numeros)
print(f"Cantidad de números positivos: {cantidad_positivos}")

#Ejercicio 6
def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    
    return lista_invertida
numeros = [1, 2, 3, 4, 5]
numeros_invertidos = invertir_lista(numeros)
print(numeros_invertidos)

#Ejercicio 7
numeros = [4, 7, 2, 9, 3, 8, 5]
suma = 0
for numero in numeros:
    suma += numero
cantidad = len(numeros)
media = suma / cantidad
print(f"La media de los números es: {media}")
