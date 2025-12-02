# README - Analizador NASDAQ con IA

## 📋 Descripción del Proyecto

**Exploración de tecnologías habilitadoras mediante proyectos básicos en Python con módulos de IA**

Este proyecto implementa un sistema automatizado de análisis financiero que combina web scraping, APIs de datos financieros e inteligencia artificial para generar reportes sobre las empresas más grandes del NASDAQ-100 (es la bolsa de valores electrónica de EE. UU. donde cotizan la mayoría de las grandes empresas tecnológicas (como Apple, Microsoft y Google)).

### ¿Qué hace el programa?

1. **Extrae datos**: Realiza web scraping para obtener las empresas actuales del NASDAQ-100 (las 100 compañías más grandes cotizadas en NASDAQ, principalmente tecnológicas)
2. **Recopila información financiera**: Utiliza la API de Finnhub para obtener datos financieros actualizados de cada empresa
3. **Ordena por capitalización**: Clasifica las empresas de mayor a menor según su valor de mercado
4. **Genera análisis con IA**: Envía la información recopilada a Gemini (modelo de IA de Google) para obtener un análisis detallado
5. **Exporta resultados**: Guarda el análisis en formato Markdown para fácil lectura y presentación

## 🏗️ Estructura del Proyecto

```
proyecto/
│
├── main.py          # Archivo principal - orquesta el flujo del programa
├── utils.py         # Funciones auxiliares y utilidades
├── data.py          # Módulo de scraping de empresas NASDAQ
├── requirements.txt # Dependencias del proyecto
├── resumen.md       # Analisis hecho por IA
└── README.md        # Este archivo

```

## 🚀 Requisitos Previos

- Python 3.8 o superior
- Clave API de Finnhub (obtenerla en [finnhub.io](https://finnhub.io/))
- Clave API de Google Gemini (obtenerla en [Google AI Studio](https://makersuite.google.com/))

## 📦 Instalación

1. **Clonar el repositorio** (o descargar los archivos)

```bash
git clone https://github.com/Sergiolpz-dev/Market-Monitor.git
cd Market-Monitor
```

2. **Crear un entorno virtual** (recomendado)

```bash
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

Crear un archivo `.env` en la raíz del proyecto con las siguientes claves:

```
FINNHUB_API_KEY=tu_clave_api_finnhub
GEMINI_API_KEY=tu_clave_api_gemini
```

## 💻 Uso

Ejecutar el programa principal:

```bash
python main.py
```

## 📝 Notas

- El NASDAQ-100 incluye las 100 empresas no financieras más grandes del NASDAQ (aunque predominan las tecnológicas)
- Se recomienda no realizar consultas excesivas a las APIs para evitar límites de tasa
- Los datos financieros reflejan información en tiempo real según la disponibilidad de la API

## 👥 Contribuciones

Este proyecto fue desarrollado como parte de una práctica académica sobre exploración de tecnologías habilitadoras con IA.

---
