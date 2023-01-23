#print("Me gusta \"Monty Python\"")

#print('Me gusta "Monty Python"')


#estamos poniendo a prueba el apareces comillas o apostrofes sin que afecten en el codigo 
#print ("I'm Monty Python.")
#print('I\'m Monty Python.')

#estamos probando cual es el resultado en cada linea segun los simvolos y la palabra verdadero y falso como boleanos 
#print(True > False)
#print(True < False)

#combinamos los caracteres aprendidos en la funcion print en una sola linea de codigo 
#pero en esta ocacion el resultado no lo de en tres lineas en consola
#print(" \"estoy\"\n \"\"aprendiendo\"\"\n\"\"\"python\"\"\"")
#print('"estoy"\n""aprendiendo""\n"""python"""')

#probando algunos tipos de operadores
#print("1.5", 2.0, 528, False)   
#print((2**0) + (2**1) + (2**3)) 
#print(1011)

#print(2+2)suma
#print(2-2)resta pero tambien anuncia si un numero en valor negativo
#print(2*2) multiplicacion
#print(2/2) division con numeros decimales en resultado
#print(2//2) ( floor division.)redondea a enteros.
#print(2%2) El resultado de la operación es el residuo que queda de la división entera.
#print(2**2) exponencial se puede utlizar en num, enteros o flotantes.
#print(2+2,2-2,2*2,2/2,2//2,2%2,2**2,sep="-") conbinando lo aprendido sev puede utilizar los \n para resultados por linea
#en cualquiera de las operaciones si algun valor els de tipo flotante el rsultado sera de tipo flot a esepcion de 
#de "/"(divicion) este siempre es flotante, sien algun casdo desea que sea de tipo entero el resultado se elplea
#la "//" pero solo si es entero los dos numeros ya que si se pone de tipo flot el resultado sera flot
#tener en cuenta que el resultado con"//" se redondendea(si el valor es negativo se redonde al siguente num negativo)
 
#print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
 

anything = input("Dime algo...")
print("Mmm...", anything, "...¿En serio?")


print("Dime algo...")
anything = input()
print("Mmm...", anything, "...¿en serio?")
