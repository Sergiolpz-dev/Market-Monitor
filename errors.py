# ===============================
#  ERRORES
# ===============================
import finnhub
import time

def obtener_candles_seguro(client, symbol, dias=30):
    try:
        end = int(time.time())
        start = end - dias*24*60*60
        ohlc = client.stock_candles(symbol, 'D', start, end)
        return ohlc
    except finnhub.FinnhubAPIException as e:
        print(f"No se pueden obtener candles para {symbol}: {e}")
        return None
    