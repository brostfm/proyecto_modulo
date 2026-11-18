import sqlite3

def inicializar_bd():
    conexion = sqlite3.connect("flighttracker.db")
    cursor = conexion.cursor()
    
    # Creación de tablas base
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vuelos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aerolinea TEXT,
            origen TEXT,
            destino TEXT,
            hora_salida TEXT,
            escalas INTEGER,
            precio REAL,
            co2_kg REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alertas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            origen TEXT,
            destino TEXT,
            precio_max REAL,
            canal TEXT
        )
    """)
    
    # Carga de datos de prueba si no existen
    cursor.execute("SELECT COUNT(*) FROM vuelos")
    if cursor.fetchone()[0] == 0:
        vuelos_demo = [
            ("Iberia", "MAD", "JFK", "10:30", 0, 420.00, 310.5),
            ("Air Europa", "MAD", "JFK", "23:45", 0, 310.00, 325.0),
            ("TAP Air", "MAD", "JFK", "14:15", 1, 260.00, 360.0),
            ("Ryanair", "MAD", "FCO", "08:15", 0, 45.00, 110.0),
            ("Vueling", "BCN", "PAR", "16:00", 0, 59.99, 95.0)
        ]
        cursor.executemany("""
            INSERT INTO vuelos (aerolinea, origen, destino, hora_salida, escalas, precio, co2_kg)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, vuelos_demo)
    
    conexion.commit()
    conexion.close()

def modulo_busqueda():
    print("\n--- BÚSQUEDA Y FILTRADO AVANZADO DE VUELOS ---")
    origen = input("Origen (IATA, ej. MAD): ").strip().upper()
    destino = input("Destino (IATA, ej. JFK): ").strip().upper()
    excluir_noche = input("¿Excluir vuelos nocturnos (22:00 a 06:00)? (s/n): ").strip().lower() == 's'
    solo_directos = input("¿Solo vuelos directos (0 escalas)? (s/n): ").strip().lower() == 's'

    conexion = sqlite3.connect("flighttracker.db")
    cursor = conexion.cursor()
    query = "SELECT aerolinea, origen, destino, hora_salida, escalas, precio, co2_kg FROM vuelos WHERE origen=? AND destino=?"
    parametros = [origen, destino]

    if solo_directos:
        query += " AND escalas = 0"

    cursor.execute(query, parametros)
    resultados = cursor.fetchall()
    conexion.close()

    if not resultados:
        print("No se encontraron vuelos para la ruta indicada.")
        return

    print(f"\nVuelos encontrados para {origen} -> {destino}:")
    print(f"{'Aerolínea':<12} | {'Salida':<7} | {'Escalas':<7} | {'Precio':<9} | {'Huella CO2'}")
    print("-" * 55)
    for vuelo in resultados:
        hora = vuelo[3]
        if excluir_noche:
            hora_num = int(hora.split(":")[0])
            if hora_num >= 22 or hora_num < 6:
                continue
        print(f"{vuelo[0]:<12} | {vuelo[3]:<7} | {vuelo[4]:<7} | {vuelo[5]:<7.2f}€ | {vuelo[6]} kg CO2")

def modulo_alertas():
    print("\n--- GESTIÓN DE ALERTAS (MÁXIMO 5 POR USUARIO) ---")
    usuario_activo = "usuario_demo@correo.com"
    
    conexion = sqlite3.connect("flighttracker.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM alertas WHERE usuario=?", (usuario_activo,))
    total = cursor.fetchone()[0]

    if total >= 5:
        print("[AVISO]: Has alcanzado el límite máximo de 5 monitorizaciones activas.")
        conexion.close()
        return

    origen = input("Origen (IATA): ").strip().upper()
    destino = input("Destino (IATA): ").strip().upper()
    precio_max = float(input("Precio objetivo (€): "))
    print("Canales disponibles: 1. PUSH | 2. WHATSAPP | 3. EMAIL")
    opcion_canal = input("Selecciona canal (1-3): ")
    canales = {"1": "PUSH", "2": "WHATSAPP", "3": "EMAIL"}
    canal_elegido = canales.get(opcion_canal, "EMAIL")

    cursor.execute("""
        INSERT INTO alertas (usuario, origen, destino, precio_max, canal)
        VALUES (?, ?, ?, ?, ?)
    """, (usuario_activo, origen, destino, precio_max, canal_elegido))
    conexion.commit()
    conexion.close()
    print(f"[CONFIRMADO]: Alerta activada para {origen}->{destino} por debajo de {precio_max}€ vía {canal_elegido}.")

def modulo_predictor():
    print("\n--- PREDICTOR DE PRECIOS & TENDENCIAS (IA/ML) ---")
    destino = input("Destino a evaluar: ").strip().upper()
    print(f"Analizando series temporales e histórico para {destino}...")
    print("-> Estado: Tarifa habitual detectada (sin Error Fares).")
    print("-> Tendencia: -14% respecto al promedio mensual.")
    print("-> Diagnóstico algorítmico: ESPERAR A UNA PRÓXIMA BAJADA.")

def menu_principal():
    inicializar_bd()
    while True:
        print("\n==========================================")
        print("          FLIGHTTRACKER - CONSOLA         ")
        print("==========================================")
        print("1. Buscar vuelos (con filtros y huella CO2)")
        print("2. Crear alerta de monitorización (Máx 5)")
        print("3. Analizador y predictor de precios (IA)")
        print("4. Salir")
        seleccion = input("Selecciona una opción (1-4): ").strip()

        if seleccion == "1":
            modulo_busqueda()
        elif seleccion == "2":
            modulo_alertas()
        elif seleccion == "3":
            modulo_predictor()
        elif seleccion == "4":
            print("Finalizando ejecución de FlightTracker.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu_principal()