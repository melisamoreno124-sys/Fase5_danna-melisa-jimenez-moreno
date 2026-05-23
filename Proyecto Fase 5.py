# =========================================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
# FASE 5 - EVALUACION FINAL POA
# ESTUDIANTE: DANNA MELISA JIMENEZ MORENO
# PROGRAMA: INGENIERIA INDUSTRIAL
# =========================================================

print("╔══════════════════════════════════════════════════════════════╗")
print("║              VIDEOTECA DIGITAL - UNAD                      ║")
print("╠══════════════════════════════════════════════════════════════╣")
print("║ Estudiante: Danna Melisa Jimenez Moreno                    ║")
print("║ Programa : Ingenieria Industrial                           ║")
print("║ Tema      : Matrices y Funciones en Python                 ║")
print("╚══════════════════════════════════════════════════════════════╝")

print("\nBienvenido al sistema de Videoteca Digital\n")

# =========================================================
# MATRIZ
# [Titulo, Año, Calificacion, Genero]
# =========================================================

videoteca = [
    ["Interestelar", 2014, 9, "Ciencia Ficcion"],
    ["Avatar", 2009, 8, "Accion"],
    ["Oppenheimer", 2023, 10, "Drama"],
    ["Toy Story", 1995, 8, "Animacion"],
    ["Duna", 2021, 9, "Ciencia Ficcion"],
    ["Joker", 2019, 8, "Drama"],
    ["The Batman", 2022, 9, "Accion"]
]

# =========================================================
# FUNCION VALIDAR NUMEROS
# =========================================================

def validar_numero(mensaje):

    while True:

        dato = input(mensaje)

        # VALIDAR SOLO NUMEROS
        if dato.isdigit():

            return int(dato)

        else:

            print("\n❌ ERROR: Debe ingresar solamente numeros.\n")

# =========================================================
# FUNCION CONTAR TITULOS
# =========================================================

def contar_titulos(matriz):

    continuar = 1

    while continuar == 1:

        # INGRESAR CALIFICACION
        calificacion_min = validar_numero(
            "\nDigite la calificacion minima (1 - 10): "
        )

        # VALIDAR RANGO
        while calificacion_min < 1 or calificacion_min > 10:

            print("\n❌ ERROR: La calificacion debe estar entre 1 y 10.\n")

            calificacion_min = validar_numero(
                "Digite nuevamente la calificacion: "
            )

        # INGRESAR AÑO
        anio_limite = validar_numero(
            "Digite el año limite: "
        )

        contador = 0

        print("\n╔════════════════════════════════════════════════════════════════════╗")
        print("║                        VIDEOTECA DIGITAL                         ║")
        print("╠════╦══════════════════╦══════╦══════════════╦════════════════════╣")
        print("║ No ║ Titulo           ║ Año  ║ Calificacion ║ Genero            ║")
        print("╠════╬══════════════════╬══════╬══════════════╬════════════════════╣")

        # RECORRER MATRIZ
        for i in range(len(matriz)):

            titulo = matriz[i][0]
            anio = matriz[i][1]
            calificacion = matriz[i][2]
            genero = matriz[i][3]

            print(f"║ {i+1:<2} ║ {titulo:<16} ║ {anio:^4} ║ {calificacion:^12} ║ {genero:<18} ║")

            # CONDICION
            if calificacion >= calificacion_min and anio >= anio_limite:

                contador += 1

        print("╚════╩══════════════════╩══════╩══════════════╩════════════════════╝")

        # RESULTADO
        print("\n╔══════════════════════════════════════╗")
        print("║           RESULTADO FINAL           ║")
        print("╠══════════════════════════════════════╣")
        print(f"║ Titulos encontrados: {contador:<16} ║")
        print("╚══════════════════════════════════════╝")

        # MENU FINAL
        print("\n========== MENU ==========")
        print("1. Realizar otra busqueda")
        print("2. Salir")

        continuar = validar_numero(
            "\nSeleccione una opcion: "
        )

        # VALIDAR OPCION
        while continuar != 1 and continuar != 2:

            print("\n❌ ERROR: Debe seleccionar 1 o 2.\n")

            continuar = validar_numero(
                "Seleccione nuevamente: "
            )

# =========================================================
# LLAMADO FUNCION
# =========================================================

contar_titulos(videoteca)

# =========================================================
# MENSAJE FINAL
# =========================================================

print("\n╔══════════════════════════════════════════════╗")
print("║      GRACIAS POR UTILIZAR EL SISTEMA        ║")
print("║          VIDEOTECA DIGITAL - UNAD           ║")
print("╚══════════════════════════════════════════════╝")
10