temperaturas = [18, 25, 31, 12, 28, 35, 20]
dias_frios = 0
dias_templados = 0
dias_calientes = 0
for temp in temperaturas:
    if temp < 15:
        print("Fria")
        dias_frios += 1
    elif temp >= 15 and temp <= 25:
        print("Templada")
        dias_templados += 1
    else:
        print("Caliente")
        dias_calientes += 1
    print(f"Temperatura: {temp}°C")
print(f"Total de días fríos: {dias_frios}")
print(f"Total de días templados: {dias_templados}")
print(f"Total de días calientes: {dias_calientes}")
