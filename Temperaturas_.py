# Definir las ciudades, semanas y días
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = 7  # Lunes a domingo
semanas = 4  # Número de semanas

# Crear la matriz 3D manualmente con valores simulados para simplificar (temperaturas en °C)
temperaturas = [
    [[18, 20, 19, 21, 22, 20, 18], [19, 22, 21, 23, 24, 20, 21], [20, 21, 19, 20, 22, 19, 21], [21, 20, 19, 21, 22, 23, 19]],  # Quito
    [[26, 28, 27, 29, 30, 28, 27], [27, 29, 28, 31, 32, 30, 29], [28, 30, 27, 29, 28, 27, 30], [29, 31, 30, 32, 33, 31, 29]],  # Guayaquil
    [[15, 17, 16, 18, 19, 16, 15], [16, 18, 17, 19, 20, 17, 16], [17, 19, 16, 18, 17, 16, 18], [18, 19, 18, 20, 21, 19, 17]]   # Cuenca
]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for ciudad in range(len(ciudades)):
    print(f"Promedios de temperatura para {ciudades[ciudad]}:")
    for semana in range(semanas):
        promedio = sum(temperaturas[ciudad][semana]) / dias_semana
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()