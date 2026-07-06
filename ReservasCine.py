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