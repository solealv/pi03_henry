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
