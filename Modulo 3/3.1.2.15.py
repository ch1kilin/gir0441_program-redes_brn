'''
Autor: ROSAS MUÑOZ ANGEL DE JESUS
Fecha: 13 de 01 del 2023
'''

numero = int(input("Ingrese un número: "))
estaResuelto = False
pasos = 0

if numero >= 1:
    while estaResuelto == False:
        if numero != 1:
            if (numero % 2) == 0:
                numero //= 2
            else:
                numero = (3 * numero) + 1

            pasos += 1
            print(numero)
        else:
            estaResuelto = True

print("pasos =", pasos)