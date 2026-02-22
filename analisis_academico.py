estudiantes = {
    "ana": [85, 90, 78],
    "luis": [60, 72, 68],
    "marta": [95, 98, 92],
    "pedro": [50, 55, 60]
}
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)
def clasificar(promedio):
    if promedio >= 90:
        return "excelente"
    elif promedio >= 70:
        return "bueno"
    elif promedio >= 50:
        return "regular"
    else:
        return "insuficiente"
def mostrar_analisis():
    if not estudiantes:
        print("no hay estudiantes registrados.")
        return
    print("\n analisis academico:")
    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        resultado = clasificar(promedio)
        print(f"- {nombre}: promedio = {promedio:.2f}, resultado = {resultado}")
def menu():
    while True:
        print("\n analisis academico ")
        print("1. mostrar analisis de estudiantes")
        print("2. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            mostrar_analisis()
        elif opcion == "2":
            print("saliendo del sistema de analisis academico.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()