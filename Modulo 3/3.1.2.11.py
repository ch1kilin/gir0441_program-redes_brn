'''
Autor: ROSAS MUÑOZ ANGEL DE JESUS
Fecha: 13 de 01 del 2023
'''


palabraSinVocal = ""
userWord = ""

userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palabraSinVocal += letra

print(palabraSinVocal)