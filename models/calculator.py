from email import header
import streamlit as st
import pandas as pd
from ftx_api import connect

def app():

    header_container = st.container()
    calculator_container = st.container()

    with header_container:
        st.image('./images/calculator.jpg')
        st.title('Calculadora de criptomonedas')
        #st.header('Utiliza la calculadora para saber el valor en dolares americanos (USD) de una criptomoneda y viceversa.')    

    with calculator_container:
        df = connect.market()
        
        cripto_list = ['BTC (Bitcoin)', 'ETH (Ethereum)', 'USDT (Tether)', 'BNB (BNB)', 'XRP (XRP)', 'SOL (Solana)', 'DOGE (Dogecoin)', 'DOT (Polkadot)', 'Dai (DAI)', 'MATIC (Polygon)']
        name_list = ['BTC/USD', 'ETH/USD', 'USDT/USD', 'BNB/USD', 'XRP/USD', 'SOL/USD', 'DOGE/USD', 'DOT/USD', 'DAI/USD', 'MATIC/USD']
        
        cri_col, usd_col = st.columns(2)
        
        ############################# Columna de cripto a dolar #############################

        cri_col.subheader('Criptomoneda -> Dolares')
        s_cripto = cri_col.selectbox('La criptomoneda que tienes:', cripto_list)
        c_cripto = float(cri_col.text_input('Cantidad', 0.0))
        
        index = cripto_list.index(s_cripto)
        valor = float(df[df['name'] == name_list[index]]['price'].values[0])
        conver_USD = valor*c_cripto
        
        cri_col.write(f'{conver_USD} USD')

        ############################# Columna de dolar a cripto #############################

        usd_col.subheader('Dolares -> Criptomoneda')
        s_usd = usd_col.selectbox('La criptomoneda que quieres:', cripto_list)
        c_usd = float(usd_col.text_input('Cantidad de USD', 0.0))
        
        index_usd = cripto_list.index(s_usd)
        valor = float(df[df['name'] == name_list[index_usd]]['price'].values[0])
        conver_cri = c_usd/valor

        usd_col.write(f'{conver_cri} {s_usd}')
    








# 'BTC (Bitcoin)', 'ETH (Ethereum)', 'USDT (Tether)', 'BNB (BNB)', 'XRP (XRP)', 'SOL (Solana)', 'DOGE (Dogecoin)', 'DOT (Polkadot)', 'Dai (DAI)', 'MATIC (Polygon)'