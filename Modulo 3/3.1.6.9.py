'''
Autor: ROSAS MUÑOZ ANGEL DE JESUS
Fecha: 13 de 01 del 2023
'''

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

listaTemp = []

for numero in miLista:
    if numero not in listaTemp:
        listaTemp.append(numero)

miLista = listaTemp[:]

print("La lista solo con elementos únicos:")
print(miLista)