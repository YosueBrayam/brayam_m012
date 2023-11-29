def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)
    

separador(3.1)
nombre= input("Cual es tu nombre?") 
print("hola",nombre,",que tal?")

separador(3.2)
Juan=3
Maria=5
Adán=6
print(Juan,Maria,Adán, sep=",") #Suma de las manzanas.

print("###########")
total_manzanas=Juan+Maria+Adán
print(total_manzanas)        #
print("############")
naranjas=(Adán+Maria*Juan)
print(naranjas, "las naranjas del suelo")

separador(3.3)


millas = 5
kilometros = millas * 1.61


print(millas, "millas son", kilometros, "kilómetros.")


kilometros = 10
millas = kilometros / 1.61
print(kilometros, "kilómetros son", millas, "millas.")

miles_to_kilometers = float(input("Ingresa la cantidad de millas a convertir a kilómetros: "))

converted_miles = miles_to_kilometers * 1.61

print(miles_to_kilometers, "millas son", converted_miles, "kilómetros.")


kilometers_to_miles = float(input("Ingresa la cantidad de kilómetros a convertir a millas: "))

converted_kilometers = kilometers_to_miles / 1.61

print(kilometers_to_miles, "kilómetros son", converted_kilometers, "millas.")

separador(3.4)


x = float(input("Ingresa un valor para x: "))


y = 3 * x**3 - 2 * x**2 + 3 * x - 1


print("El resultado de la expresión 3x^3 - 2x^2 + 3x - 1 para x =", x, "es y =", y)

separador(3.5)

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
coste_por_hora = float(input("Ingrese el coste por hora: "))


paga_total = horas_trabajadas * coste_por_hora

print(f"La paga total es: ${paga_total:.2f}")

separador(3.6)

#
n = int(input("Ingrese un entero positivo: "))


if n <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    
    suma = (n * (n + 1)) // 2  

    print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")



separador(3.7)

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))


imc = peso / (estatura**2)


imc_redondeado = round(imc, 2)

print(f"Tu índice de masa corporal es {imc_redondeado}")


separador(3.8)


cantidad_invertida = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual en porcentaje: "))
anios = int(input("Ingrese el número de años: "))


capital_obtenido = cantidad_invertida * (1 + (interes_anual / 100))**anios

print(f"El capital obtenido en la inversión después de {anios} años es: {capital_obtenido:.2f}")


separador(3.9)

byte1 = int(input("Ingrese el primer byte de la dirección IP: "))
byte2 = int(input("Ingrese el segundo byte de la dirección IP: "))
byte3 = int(input("Ingrese el tercer byte de la dirección IP: "))
byte4 = int(input("Ingrese el cuarto byte de la dirección IP: "))


if 0 <= byte1 <= 255 and 0 <= byte2 <= 255 and 0 <= byte3 <= 255 and 0 <= byte4 <= 255:

    direccion_ip = f"{byte1}.{byte2}.{byte3}.{byte4}"
    print("La dirección IP es:", direccion_ip)
else:
    print("Los bytes deben estar en el rango válido (0-255).")
