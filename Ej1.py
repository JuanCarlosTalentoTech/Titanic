# Hola mundo
print("Hola mundo")

# Crea un programa para saber si un número es par o impar

try:
    # Solicitamos al usuario que ingrese un número
    numero = int(input("Introduce un número entero: "))
    
    # Un número es par si el resto de su división entre 2 es 0
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
except ValueError:
    print("Error: Por favor, ingresa un número entero válido.")


