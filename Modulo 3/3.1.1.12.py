'''
Descripccion:Utilizar la sentencia if-elif-else.
Autor: ROSAS MUÑOZ ANGEL DE JESUS
Fecha: 13 de 01 del 2023
'''

year = int(input("Introduce un año:"))

if year % 4 !=0: #No es divisible entre 4
   print('Año común')
elif year % 100 !=0: #año Bisiesto
   
   print('Año Bisiesto')
elif year % 400  !=0: 
    print('Año Comun')
else:
   print('De lo contrario, es un año bisisesto')