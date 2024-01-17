# Definición de funciones
def obtener_datos():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Ejecución del programa
datos = obtener_datos()
promedio = calcular_promedio(datos)
print(f"El promedio semanal del clima es: {promedio}")