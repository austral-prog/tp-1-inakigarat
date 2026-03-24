def age():
    """
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """
    edad_anos = 25
    edad_meses = edad_anos * 12
    edad_dias = edad_anos * 365
    edad_horas = edad_anos * 24
    edad_minutos = edad_anos * 60

    print("edad en meses", edad_meses)
    print("edad en dias", edad_dias)
    print("edad en horas", edad_horas)
    print("edad en minutos", edad_minutos)

age()

