"""
Nombre: angel de jesus rosas muñoz
Fecha: 13/01/23
Descripción:  Tomara horas y minutos , y tiempo restante para que termine una determinada hora  
"""

horas=int(input("Hora de inicio (horas): "))
minutos=int(input("Minuto de inicio (minutos): "))
duracion=int(input("Duración del evento (minutos): "))


#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
#datos de prueba
#horas = 23; minutos = 58; duracion = 642
horasDia = 24
minutosHora = 60

minutos += duracion
horasQueMePase = minutos // minutosHora
minutos = minutos % minutosHora

horas += horasQueMePase
horas = horas % horasDia

print('El evento termina a las ' + str(horas) + ' : ' +str(minutos))
