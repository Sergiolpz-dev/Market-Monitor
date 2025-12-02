import finnhub
import time
from datetime import datetime, timedelta
import pandas as pd

# ===============================
#  FUNCIONES
# ===============================

# Crea y retorna un cliente de la API de Finnhub usando la clave API proporcionada
def crear_cliente(api_key):
    return finnhub.Client(api_key=api_key)

# Obtiene la cotización actual (precio y datos relacionados) de un símbolo bursátil
def get_quote(symbol, client):
    try:
        return client.quote(symbol)
    except:
        return None

# Obtiene el perfil de la empresa (información básica como nombre, sector, website, etc.)
def get_profile(symbol, client):
    try:
        return client.company_profile2(symbol=symbol) 
    except:
        return None

# Obtiene las tendencias de recomendaciones de analistas (comprar, mantener, vender) para un símbolo
def get_recommendations(symbol, client):
    try:
        data = client.recommendation_trends(symbol)
        if data:
            return data[0]
        return None
    except:
        return None


# Ordena los resultados por capitalización de mercado de mayor a menor y retorna un DataFrame de Pandas
def sortByMarketCap(results):
    results = sorted(
        results,
        key=lambda x: (x['market_cap'] is None, x['market_cap'] or 0),
        reverse=True
    )
    # Opcional: Configurar Pandas para mostrar números grandes sin notación científica
    pd.options.display.float_format = '{:,.0f}'.format
    df = pd.DataFrame(results)
    return df