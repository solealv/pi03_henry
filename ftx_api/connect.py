import requests
import pandas as pd

def single_market(market):
    url = f'https://ftx.com/api/markets/{market}/candles?resolution=86400'
    response = requests.get(url)
    sng_mkt = pd.DataFrame(response.json()['result'])
    sng_mkt.rename(columns={'time':'time_num'}, inplace = True)
    sng_mkt['startTime'] = pd.to_datetime(sng_mkt['startTime'])
    sng_mkt.insert(2, 'date', sng_mkt.startTime.dt.date)
    sng_mkt.insert(3, 'time', sng_mkt.startTime.dt.time)
    sng_mkt.drop(columns='startTime', inplace = True)
    return sng_mkt

def market():
    url = 'https://ftx.com/api/markets'
    response = requests.get(url)
    mkt = pd.DataFrame(response.json()['result'])
    return mkt

def grafic_data(coin):
    df = single_market(coin)
    df['close_m10'] = df['close'].rolling(10).mean()
    df['close_std'] = df['close'].rolling(5).std()
    df['bottom'] = df.close - df.close_std
    df['top'] = df.close + df.close_std
    df['MA10'] = df.close_m10
    df.drop(columns=['time_num', 'time','open', 'high', 'low'], inplace=True)
    return df

# Vamos a basar el analisis en las 10 monedas que poseen la mayor capitalizacion del mercado y
# que se encuentren en la plataforma de FTX:
# BTC (Bitcoin), ETH(Ethereum), USDT (Tether),
# BNB (BNB), XRP (XRP), SOL (Solana),
# DOGE (Dogecoin), DOT (Polkadot), Dai (DAI)
# MATIC (Polygon)

cripto_list = ['BTC (Bitcoin)', 'ETH (Ethereum)', 'USDT (Tether)', 'BNB (BNB)', 'XRP (XRP)', 'SOL (Solana)', 'DOGE (Dogecoin)', 'DOT (Polkadot)', 'Dai (DAI)', 'MATIC (Polygon)']
name_list = ['BTC/USD', 'ETH/USD', 'USDT/USD', 'BNB/USD', 'XRP/USD', 'SOL/USD', 'DOGE/USD', 'DOT/USD', 'DAI/USD', 'MATIC/USD']

BTC = 'Bitcoin es la primera y principal criptomoneda del mercado. Se considera la referencia del mercado, hay que tener en cuenta que la capitalización de mercado de Bitcoin es superior a la de la suma de todas las demás criptomonedas (existen varios miles de criptomonedas).'
ETH = 'La altcoin mejor posicionada en el mercado es Ethereum. El principal valor de Ethereum es su blockchain propia (considerada de segunda generación) y la posibilidad de hacer contratos inteligentes o smart contracts, crear aplicaciones basadas en la blockchain o emitiar tokens.'
USDT = 'Los tokens Tether se conocen como monedas estables porque ofrecen estabilidad de precios ya que están vinculados a una moneda fiduciaria. Esto ofrece a los comerciantes, comerciantes y fondos una solución de baja volatilidad al salir de posiciones en el mercado. Todos los tokens de Tether están vinculados 1 a 1 con una moneda fiduciaria correspondiente (por ejemplo, 1 USD₮ = 1 USD) y están respaldados al 100 % por las reservas de Tether.'
BNB = 'BNB o Binance Coin es un Token de la plataforma Binance. Se podría considerar como una moneda digital de Binance. De hecho, en el ranking de criptomonedas por capitalización de mercado (incluyendo Tokens) actualmente es la tercera, sólo por detrás de Bitcoin y Ethereum. Esta criptomoneda se lanzó sobre la cadena de bloques de Ethereum, concretamente con la forma de un Token ERC-20.'
XRP = 'Ripple fue presentada en 2012 como una nueva plataforma para realizar pagos. Opera en el mercado de las criptomonedas con la suya propia, el XRP. Esta última tiene distintas características que la hacen particular, con respecto a otras. Ripple, por ejemplo, es mucho más rápido a la hora de realizar las validaciones, por lo que sus transacciones son realmente ágiles.'
SOL = 'Solana es un tipo de blockchain (cadena de bloques) para impulsar el desarrollo de apps descentralizadas (DApps) y cuyo servicio consiste en aportar seguridad a estas aplicaciones. También es una criptomoneda sobre la que invertir'
DOGE = 'Dogecoin es una criptomoneda cuya función principal es servir como medio de pago. La misma fue promovida o pompeada especialmente por Elon Musk a través de su Twitter y ha llegao a convertirse en la cuarta moneda digital más grande. A pesar de esto, en el mercado se la considera una “shitcoins” o criptomoneda basura. Este tipo de criptomoneda son monedas que no aportan valor alguno a la blockchain y no tienen ningún tipo de desarrollo, innovación ni utilidad para la comunidad. Salen al mercado con el único propósito de especular con su valor, suelen ser extremadamente volátiles y te pueden hacer ganar o perder mucho dinero en poco tiempo.'
DOT = 'Polkadot tiene su propia blockchain, pero a diferencia de las anteriores esta pretende conectar entre sí las diferentes blockchains para que se pueda cruzar o consultar la información de diferentes blockchains en un mismo lugar.'
DAI = 'Dai (o DAI) es una criptomoneda estable que tiene como objetivo mantener su valor lo más cercano posible al dólar estadounidense (USD) a través de un sistema automatizado de contratos inteligentes en la cadena de bloques de Ethereum.1 Dai se mantiene y regula por MakerDAO, una organización autónoma descentralizada (DAO) compuesta por los propietarios de su token de gobernanza, MKR. Para garantizar la estabilidad del Dai, sus propietarios pueden votar los cambios de ciertos parámetros en sus contratos inteligentes.'
MATIC = 'La red del MATIC es un protocolo que permite aumentar la escalabilidad de la cadena de bloques Ethereum y sumar nuevos casos de uso. Polygon funciona a través de una sidechain (cadena lateral) que se conecta a Ethereum permitiendo un mayor procesamiento'

ref_list = [BTC, ETH, USDT, BNB, XRP, SOL, DOGE, DOT, DAI, MATIC]