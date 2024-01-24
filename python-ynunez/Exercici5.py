def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(5.1)



for i in range(1, 6):
    print(i, "Mississippi")
print("¡Listos o no, ahí voy!")


separador(5.2)

while True:
    word = input("Ingresa una palabra: ")
    if word == "chupacabra":
        print("¡Has dejado el bucle con éxito!")
        break

separador(5.3)


user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue
    else:
        word_without_vowels += letter

print(word_without_vowels)



separador(5.5)

amount = float(input("¿Cuantitat a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Anys?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))


separador(5.6)

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

separador(5.7)

n = int(input("Introduce un número entero: "))

es_primo = True

for i in range(2, n):
    if n % i == 0:
        es_primo = False
        break

if es_primo:
    print(n, "es un número primo.")
else:
    print(n, "no es un número primo.")

separador(5.8)


palabra = input("Introduce una palabra: ")


resultado = ""


for i in range(len(palabra) - 1, -1, -1):
    resultado += palabra[i] + "\n"

print(resultado)

separador(5.9)

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

contador = 0

for c in frase:
    if c == letra:
        contador += 1

print("La letra", letra, "aparece", contador, "veces en la frase.")


separador (5.10)

blocks = int(input("Ingresa el número de bloques: "))

height = 0

layer = 1

while blocks >= layer:
    height += 1
    blocks -= layer
    layer += 1

print("La altura de la pirámide:", height)
