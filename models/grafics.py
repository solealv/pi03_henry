from turtle import width
import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from ftx_api import connect

def app():

    header_container = st.container()
    price_container = st.container()

    with header_container:
        st.image('./images/photo.jpg')
        st.title('Graficos')
        st.header('Precio historico - Varianza - Media movil')    

    with price_container:
        
        cripto_list = ['BTC (Bitcoin)', 'ETH (Ethereum)', 'USDT (Tether)', 'BNB (BNB)', 'XRP (XRP)', 'SOL (Solana)', 'DOGE (Dogecoin)', 'DOT (Polkadot)', 'Dai (DAI)', 'MATIC (Polygon)']
        name_list = ['BTC/USD', 'ETH/USD', 'USDT/USD', 'BNB/USD', 'XRP/USD', 'SOL/USD', 'DOGE/USD', 'DOT/USD', 'DAI/USD', 'MATIC/USD']
        
        s_cripto = st.selectbox('La criptomoneda que quieres ver:', cripto_list)
        index = cripto_list.index(s_cripto)

        df = connect.grafic_data(name_list[index])
        
        st.subheader('Precios historicos')
        fig = go.Figure([
            go.Scatter(
                name='Close price',
                x=df.date.values,
                y=df.close.values,
                mode='lines',
                marker=dict(color='#E8E9D5', size=2),
                line=dict(width=2),
                showlegend=True
            ),
            go.Scatter(
                name='Upper Bound',
                x=df.date.values,
                y=df.top.values,
                mode='lines',
                marker=dict(color='#3BA52A'),
                line=dict(width=1),
                showlegend=True
            ),
            go.Scatter(
                name='Lower Bound',
                x=df.date.values,
                y=df.bottom.values ,
                marker=dict(color='#BA1717'),
                line=dict(width=1),
                mode='lines',
                fillcolor='rgba(244, 244, 244, 0.3)',
                fill='tonexty',
                showlegend=True
            ),
            go.Scatter(
                name='MA10',
                x=df.date.values,
                y=df.MA10.values ,
                marker=dict(color='#B5BE13'),
                line=dict(width=2),
                mode='lines',
                showlegend=True
            )
        ])
        fig.update_layout(
            width = 800,
            height = 300,
            margin=dict(l=1, r=1, b=1, t=30),
            yaxis_title='USD $',
            hovermode="x"
        )
        
        st.write(fig)


        st.subheader('Volumenes de transaccion historicos')
        fig2 = go.Figure([
            go.Scatter(
            name='Volume',
            x=df.date.values,
            y=df.volume.values,
            mode='lines',
            marker=dict(color='#5B63BD', size=2),
            line=dict(width=1),
            showlegend=True
        )])
        fig2.update_layout(
            width = 770,
            height = 300,
            margin=dict(l=1, r=1, b=1, t=30),
            yaxis_title='Volumen en USD $',
            hovermode='x'
            )
        
        st.write(fig2)

