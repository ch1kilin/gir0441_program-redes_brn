"""
Nombre: angel de jesus rosas muñoz
Fecha: 13/01/23
Descripción:  Mostrar las millas en kilometros y kilometros en millas 
"""

kilometers = 12.25
miles = 7.38

miles_to_kilometers = (miles * 1.61)
kilometers_to_miles = (kilometers / 1.61)

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

