import finnhub
import pandas as pd
from datetime import datetime, timedelta

# Importación de Google GenAI NECESARIA
from google import genai 
from google.genai import types

# Configuración
import os
from dotenv import load_dotenv
load_dotenv()
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Funciones
from utils import crear_cliente, get_quote, get_profile, get_recommendations, sortByMarketCap
# Datos
from data import NASDAQ100


# Cliente Finnhub
client = crear_cliente(FINNHUB_API_KEY) 

# Resultados
unsortedResults = []

n_empresas=20

print(f"\n📊 Obteniendo datos del Nasdaq {n_empresas}...\n")

for symbol in NASDAQ100[:n_empresas]:  
    quote = get_quote(symbol, client)
    profile = get_profile(symbol, client)
    reco = get_recommendations(symbol, client)

    unsortedResults.append({
        "symbol": symbol,
        "price": quote["c"] if quote else None,
        "market_cap": profile.get("marketCapitalization") if profile else None,
        "industry": profile.get("finnhubIndustry") if profile else None,
        "analyst_buy": reco.get("buy") if reco else None,
        # "news_summaries": headlines
    })

# Ordenar por capitalización de mercado
results = sortByMarketCap(unsortedResults)
print(results)

# =========================================================================
# === CONEXIÓN Y GENERACIÓN DE CONTENIDO CON GEMINI ===
# =========================================================================

# Inicializar Cliente Gemini
# La clave API se lee automáticamente de la variable de entorno GEMINI_API_KEY
client_gemini = None
try:
    # 🛑 CAMBIO CLAVE AQUÍ: Pasamos el valor de la clave que leímos al inicio
    # Esto garantiza que el cliente se inicialice correctamente con tu valor.
    if GEMINI_API_KEY:
        client_gemini = genai.Client(api_key=GEMINI_API_KEY)
    else:
        # Lanza el error si la variable no se pudo leer
        raise ValueError("La variable GEMINI_API_KEY no se encontró.")

except Exception as e:
    # Se añade un manejo de error
    print(f"⚠️ ADVERTENCIA: Error al inicializar el cliente Gemini. {e}")
    print("El análisis de Gemini no se ejecutará.")

if client_gemini:
    print("\n" + "="*50)
    print("🤖 Procesando y enviando datos a Gemini...")
    print("="*50)
    
    # 1. CONVERTIR A DATAFRAME Y PREPARAR DATOS
    # Convertir la lista 'results' en un DataFrame
    df_results = pd.DataFrame(results)
    
    # Ajuste de formato: Convertir la capitalización de mercado a miles de millones (Billion) 
    # y asegurarse de manejar posibles valores None o NaN.
    # Asume que Finnhub da la capitalización en USD
    df_results['market_cap_B'] = df_results['market_cap'].apply(lambda x: x / 1_000_000_000 if x is not None else None)
    df_results = df_results.drop(columns=['market_cap'])
    df_results = df_results.rename(columns={'market_cap_B': 'market_cap (Billion USD)'})
    
    # Convertir el DataFrame final a formato Markdown
    datos_md = df_results.to_markdown(index=False, floatfmt=".2f")
    
    # 2. CONSTRUCCIÓN DEL PROMPT
    prompt = f"""
    Eres un analista de mercado experto. Basándote en los siguientes datos de las principales empresas del NASDAQ 100, genera un resumen de análisis de mercado exhaustivo y proporciona expectativas de inversión.

    **Instrucciones de Formato y Contenido:**

    1.  El resultado debe estar completamente en **formato Markdown (MD)**, usando encabezados (##), listas (*) y negritas.
    2.  **Sección 1: Resumen de Tendencias.** Identifica las dos industrias más representadas en el conjunto de datos y comenta la tendencia general observada en el respaldo de analistas ('analyst_buy') para esas industrias.
    3.  **Sección 2: Expectativas por Consenso (Top 3).** Analiza las 3 empresas con la **mayor combinación de 'market_cap' y 'analyst_buy'**. Para cada una, proporciona una **perspectiva de expectativas** a corto plazo (por qué su puntuación de 'analyst_buy' es un buen o mal indicador).

    ---
    **DATOS DE ENTRADA:**
    {datos_md}
    """
    
    # 3. LLAMADA A LA API DE GEMINI Y ESCRITURA EN ARCHIVO
    try:
        response = client_gemini.models.generate_content(
            model='gemini-2.5-flash',  
            contents=prompt
        )
        
        # 🟢 CAMBIO CLAVE AQUÍ: Escritura del resultado en resumen.md
        nombre_archivo = "resumen.md"
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            file.write(response.text)
        
        # Confirmación
        print("\n" + "="*50)
        print(f"✅ ANÁLISIS GENERADO Y GUARDADO EN: {nombre_archivo}")
        print("="*50)
        
    except Exception as e:
        print(f"\n❌ ERROR al llamar a la API de Gemini: {e}")

else:
    print("\nEl análisis de Gemini fue omitido. Por favor, configura tu GEMINI_API_KEY.")