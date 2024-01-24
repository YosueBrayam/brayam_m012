def separador(exercici):
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(6.1)


c0 = int(input("Ingresa un número natural: "))


steps = 0

while c0 != 1:
   
    if c0 % 2 == 0:
        c0 = c0 // 2
  
    else:
        c0 = 3 * c0 + 1
   
    steps += 1
   
    print(c0)


print("Se necesitaron", steps, "pasos para llegar a 1")


separador (6.2)


lista = [1, 2, 3, 4, 5]


numero = int(input("Ingresa un número entero: "))


lista[2] = numero

lista.pop()


print(len(lista))
