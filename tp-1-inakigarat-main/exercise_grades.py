def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9

    print("El promedio de las tres notas", (nota1 + nota2 + nota3)/3)
    print("la nota maxima", max(nota1, nota2, nota3))
    print("la nota minima", min(nota1, nota2, nota3))
    print("cuantos puntos faltan del promedio a 10", 10 - ((nota1 + nota2 + nota3)/3))

if __name__ == '__main__':
        grades()