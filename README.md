# ⏱️ Cronómetro Pro Moderno (CustomTkinter)

Una aplicación de escritorio moderna, minimalista y de alto rendimiento desarrollada en **Python** utilizando **CustomTkinter**. El proyecto implementa una arquitectura limpia basada en el patrón de diseño **MVC (Modelo-Vista-Controlador)**, optimizando el rendimiento, la mantenibilidad del código y ofreciendo una interfaz de usuario (UI/UX) atractiva.

---

## 🎨 Características Principales

- **Diseño Moderno & UI/UX Premium:** Interfaz oscura (Dark Mode por defecto) con bordes estilizados, contenedores tipo tarjeta y tipografías legibles.
- **Métricas de Tiempo en Tiempo Real:** 
  - ⚡ **Tiempo Más Corto:** Registra tu mejor marca (Best Lap).
  - 🐢 **Tiempo Más Largo:** Mantiene el registro de la duración máxima.
  - 📊 **Promedio:** Calcula en tiempo real la media aritmética de todos los tiempos guardados.
- **Arquitectura Modular (MVC):** Separación total de responsabilidades entre lógica de negocio, interfaz gráfica y control de eventos.
- **Optimización de Código:** Uso eficiente de métodos compactos y estructuras en una sola línea donde corresponde para mantener ligereza.

---

## 📂 Estructura del Proyecto

```text
Cronometro/
│
├── modules/
│   ├── __init__.py           # Identificador de paquete de módulos
│   ├── time_model.py         # Lógica de cálculo, formatos y métricas (Model)
│   ├── chrono_view.py        # Componentes y widgets de la UI (View)
│   └── chrono_controller.py  # Conector entre eventos UI y lógica (Controller)
│
└── main.py                   # Punto de entrada de la aplicación
```

---

## 🚀 Requisitos e Instalación

### Requisitos Previos
- **Python 3.10+**
- **CustomTkinter**

### Instalación de Dependencias
Asegúrate de instalar la librería gráfica antes de ejecutar la aplicación:

```bash
pip install customtkinter
```

---

## 🛠️ Ejecución del Proyecto

Para iniciar la aplicación, ejecuta el archivo principal desde la raíz de tu proyecto:

```bash
python main.py
```

---

## 🏗️ Arquitectura y Diseño del Código

1. **`TimeModel` (`modules/time_model.py`):**
   Mantiene el estado global del temporizador, calcula los valores mínimos, máximos y promedios, además de manejar el formateo dinámico de cadenas de texto.
   
2. **`ChronoView` (`modules/chrono_view.py`):**
   Construye la interfaz visual usando la rejilla de CustomTkinter. Administra el cambio visual de estados en el botón principal (Verde = Iniciar, Rojo = Detener).

3. **`ChronoController` (`modules/chrono_controller.py`):**
   Maneja el bucle recursivo de tiempo (`app.after`) y la sincronización entre el modelo y la vista.

---

## ✒️ Licencia

Este proyecto se encuentra disponible como software de código abierto bajo la licencia MIT.