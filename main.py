import finnhub
import pandas as pd
from datetime import datetime, timedelta
from transformers import pipeline

# Configuración
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Funciones
from utils import crear_cliente, get_quote, get_profile, get_recommendations, get_news, summarize, sortByMarketCap
# Datos
from data import NASDAQ100


# Cliente Finnhub
client = crear_cliente(API_KEY) 

# IA: resumen noticias
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Resultados
results = []

print("\n📊 Obteniendo datos del Nasdaq 100...\n")

for symbol in NASDAQ100[:40]:  # ← SOLO 10 para ir rápido al principio
    quote = get_quote(symbol, client)
    profile = get_profile(symbol, client)
    reco = get_recommendations(symbol, client)
    news = get_news(symbol, client)

    # # Resumir 1-2 noticias
    # headlines = []
    # for n in news[:2]:
    #     summary = summarize(n["headline"], summarizer)
    #     headlines.append(summary)

    results.append({
        "symbol": symbol,
        "price": quote["c"] if quote else None,
        "market_cap": profile.get("marketCapitalization") if profile else None,
        "industry": profile.get("finnhubIndustry") if profile else None,
        "analyst_buy": reco.get("buy") if reco else None,
        # "news_summaries": headlines
    })

# Ordenar por capitalización de mercado
print(sortByMarketCap(results))
