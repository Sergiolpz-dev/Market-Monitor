
# Scrapear nombres actualizados del Nasdaq 100

import pandas as pd 

# Deslimitamos la salida de pandas
pd.set_option('display.max_rows', None)

# URL de la página con la lista de componentes del NASDAQ 100
url = 'https://www.slickcharts.com/nasdaq100'

# Pandas lee todas las tablas HTML de la página. La lista de componentes suele ser la primera [0]
tablas_nasdaq = pd.read_html(url)

# Asumimos que la tabla de componentes es la primera (índice 0)
df_nasdaq100 = tablas_nasdaq[0]

# Selecciona solo las columnas del símbolo ('Symbol') y el nombre ('Company')

NASDAQ100 = df_nasdaq100['Symbol'].tolist()
# peperoni = df_nasdaq100['Company'].tolist()
# NASDAQ100 = df_nasdaq100[['Symbol','Company']].values.tolist()
# print(NASDAQ100)


# NASDAQ100 sabado = [
#     "AAPL","MSFT","AMZN","NVDA","META","GOOGL","GOOG","TSLA","PEP","COST",
#     "AVGO","ADBE","NFLX","CMCSA","AMD","INTC","CSCO","QCOM","TXN","AMAT",
#     "INTU","SBUX","ISRG","BKNG","GILD","VRTX","REGN","LRCX","ADI","MDLZ",
#     "PYPL","PDD","HON","AMGN","MU","ADP","ABNB","CRWD","MAR","PNC",
#     "CTAS","KLAC","MELI","SNPS","CDNS","KDP","MRNA","AEP","XEL","FTNT",
#     "PANW","ORLY","PAYX","NXPI","EA","IDXX","ODFL","CSX","CHTR","PCAR",
#     "ROP","MNST","ALGN","TEAM","CTSH","EXC","DXCM","VRSK","AZN","BIIB",
#     "SGEN","WDAY","ZS","LCID","BKR","CPRT","CCEP","KHC","MRVL","SWKS",
#     "SPLK","ANSS","VRSN","CDW","DLTR","ROST","WBD","GEN","INCY","DOCU"
# ]