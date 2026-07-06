# Datos iniciales (películas, horarios, capacidad)
peliculas = {
    1: {"nombre": "Cuarto para Nadie", "horarios": {1: {"hora": "18:00", "capacidad": 50, "vendidos": 0},
                                             2: {"hora": "20:00", "capacidad": 50, "vendidos": 0}}},
    2: {"nombre": "La Boca del Pasillo", "horarios": {1: {"hora": "19:00", "capacidad": 30, "vendidos": 0},
                                             2: {"hora": "21:00", "capacidad": 30, "vendidos": 0}}}
}

precio_entrada = 100  # Precio base
promocion_2x1 = True  # Ejemplo simple de promoción 2x1

# Variables para estadísticas
estadisticas = {
    "ventas_pelicula": {1: 0, 2: 0},
    "ventas_horario": {(1,1): 0, (1,2): 0, (2,1): 0, (2,2): 0},
    "total_entradas": 0
}

def mostrar_peliculas():
    print("Películas disponibles:")
    for clave, valor in peliculas.items():
        print(f"{clave}. {valor['nombre']}")

def mostrar_horarios(pelicula_id):
    print(f"Horarios para {peliculas[pelicula_id]['nombre']}:")
    for clave, info in peliculas[pelicula_id]['horarios'].items():
        disponibilidad = info['capacidad'] - info['vendidos']
        print(f"{clave}. {info['hora']} - Entradas disponibles: {disponibilidad}")

def reservar_entradas():
    while True:
        try:
            mostrar_peliculas()
            pelicula_id = int(input("Seleccione la película (número): "))
            if pelicula_id not in peliculas:
                print("Película no válida, intente de nuevo.")
                continue

            mostrar_horarios(pelicula_id)
            horario_id = int(input("Seleccione el horario (número): "))
            if horario_id not in peliculas[pelicula_id]['horarios']:
                print("Horario no válido, intente de nuevo.")
                continue

            entradas = int(input("Cantidad de entradas a reservar: "))
            if entradas <= 0:
                print("Debe ingresar una cantidad positiva.")
                continue

            capacidad = peliculas[pelicula_id]['horarios'][horario_id]['capacidad']
            vendidos = peliculas[pelicula_id]['horarios'][horario_id]['vendidos']

            if entradas > (capacidad - vendidos):
                print("No hay suficientes entradas disponibles para ese horario.")
                continue

            # Cálculo de importe con promoción simple 2x1
            if promocion_2x1:
                entradas_a_pagar = (entradas // 2) + (entradas % 2)
            else:
                entradas_a_pagar = entradas

            importe_total = entradas_a_pagar * precio_entrada

            confirmar = input(f"Importe total: ${importe_total}. Confirmar reserva (s/n): ").lower()
            if confirmar != 's':
                print("Reserva cancelada.")
                return  

            # Reservar actualizando datos
            peliculas[pelicula_id]['horarios'][horario_id]['vendidos'] += entradas
            estadisticas['ventas_pelicula'][pelicula_id] += entradas
            estadisticas['ventas_horario'][(pelicula_id, horario_id)] += entradas
            estadisticas['total_entradas'] += entradas

            print("Reserva exitosa.")
            return
        except ValueError:
            print("Entrada inválida, por favor ingrese un número.")

def mostrar_estadisticas():
    print("\n----- Estadísticas -----")
    print("Películas más elegidas:")
    for pid, total in estadisticas['ventas_pelicula'].items():
        print(f"{peliculas[pid]['nombre']}: {total} entradas")

    print("\nHorarios con mayor demanda:")
    for (pid, hid), total in estadisticas['ventas_horario'].items():
        if total > 0:
            print(f"{peliculas[pid]['nombre']} - {peliculas[pid]['horarios'][hid]['hora']}: {total} entradas")

    print(f"\nTotal de entradas vendidas: {estadisticas['total_entradas']}\n")            
