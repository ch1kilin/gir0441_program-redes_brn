'''
Descripccion:Utilizar el bucle while.
Autor: ROSAS MUÑOZ ANGEL DE JESUS
Fecha: 13 de 01 del 2023
'''

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

number = int(input())

while secret_number != number: 
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!" )
    
    

    print(
    """
    +==================================+
    | ¡Bienvenido a mi juego, muggle!  |
    | Introduce un número entero       |
    | y adivina qué número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¿Cuál es el número secreto?      |
    +==================================+
    """)

    number = int(input())
print ('ADIOS')