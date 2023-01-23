'''
Autor: ROSAS MUÑOZ ANGEL DE JESUS
Fecha: 13 de 01 del 2023
descripcion: Para este ejercicio utilice las condicionales y los if, todo con el fin de revisar si el año es bisiesto o si es un año comun
podemos ver que el if cumple la funcion de en caso de no ser año bisiesto, indica que es año normal y asi puede ver las vueltas y los años
'''

def isYearLeap(year):
    esBisiesto = False
    divisibleEntre_4 = year % 4
    divisibleEntre_100 = year % 100
    divisibleEntre_400 = year % 400

    if year >= 1582:
        if divisibleEntre_4 != 0:
            esBisiesto = False
        elif divisibleEntre_100 != 0:
            esBisiesto = True
        elif divisibleEntre_400 != 0:
            esBisiesto = False
        else:
            esBisiesto = True
    else:
        esBisiesto = False

    return esBisiesto


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Error")