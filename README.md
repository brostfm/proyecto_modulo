# FlightTracker - Proyecto de Módulo (DAM)

Sistema de gestión, búsqueda y monitorización de vuelos desarrollado en Python con persistencia en SQLite para el módulo de Desarrollo de Aplicaciones Multiplataforma (DAM).

---

## 📌 Descripción del Proyecto

**FlightTracker** es una aplicación de consola orientada a facilitar la consulta de vuelos, el cálculo de impacto ambiental mediante huella de CO₂, y la gestión inteligente de alertas de precios con análisis predictivo de tendencias.

---

## 🚀 Funcionalidades Principales

1. **Búsqueda y Filtrado Avanzado de Vuelos**:
   - Búsqueda por códigos IATA de origen y destino (ej. `MAD` -> `JFK`).
   - Filtro para exclusión de vuelos nocturnos (entre 22:00 y 06:00).
   - Filtro exclusivo para vuelos directos (0 escalas).
   - Visualización de precios y estimación de huella de carbono (`CO₂ kg`).

2. **Gestión de Alertas de Monitorización**:
   - Creación de alertas configurables con precio objetivo.
   - Restricción de límite operativo (máximo 5 alertas activas por usuario).
   - Notificación multicanal: `PUSH`, `WHATSAPP` o `EMAIL`.

3. **Predictor de Precios y Tendencias**:
   - Evaluación algorítmica de series temporales y detección de tarifas anómalas (*error fares*).
   - Diagnóstico predictivo de compra recomendada vs. espera de bajada de precios.

4. **Persistencia de Datos**:
   - Base de datos relacional SQLite (`flighttracker.db`) con esquema automático y carga inicial de datos de prueba (*seed data*).

---

## 🛠️ Requisitos e Instalación

- **Python**: Versión 3.8 o superior.
- **Módulos**: Utiliza únicamente la librería estándar de Python (`sqlite3`), por lo que no requiere dependencias externas adicionales.

### Ejecución

Clonar el repositorio y ejecutar el archivo principal:

```bash
python proyecto.py
```

---

## 📂 Estructura del Proyecto

```text
proyecto_modulo/
├── flighttracker.db    # Base de datos SQLite (tablas vuelos y alertas)
├── proyecto.py         # Código fuente principal de la aplicación
├── .gitignore          # Exclusiones de Git
└── README.md           # Documentación del proyecto
```

---

## 🔄 Control de Versiones y Seguimiento

Este repositorio se actualiza de forma continua con cada hito y avance del proyecto. Las versiones y snapshots pueden consultarse en el historial de commits y etiquetas del repositorio.
