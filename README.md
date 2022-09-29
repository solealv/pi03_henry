# Introducción
Este repositorio corresponde a un trabajo de visualizacion de datos que realicé como estudiante del Bootcamp de Data Science de Henry.

## Consigna
Conectar la API de FTX a un dashboard y cumplir con los siguientes requisitos:<br>

* Reporte de calidad y detalle de los datos: Esto quiere decir que deberán crear una documentación en la cuál expliquen qué es cada dato con el cuál decidieron trabajar y, además, su calidad.
* Se debe trabajar directamente con conexión a la API. Es decir que su trabajo no puede estar montado a partir de archivos csv o de entorno local.
* Deberán elegir 10 criptomonedas para el reporte.<br>

El Dashboard puede armarse en PowerBI o Streamlit. Este mismo deberá contar con:<br>
* Interacción para la búsqueda de datos históricos de precio de diferentes monedas.
* Volumen de transacción.
* Varianza.
* Calculadora. Esta misma deberá arrojar el precio a partir de la paridad, es decir, podremos pedir el valor en USD a partir de una suma de BTC o viceversa.
* Media Móvil.

## Descripcion
Para llevar a cabo este trabajo realice el Dashboard con Streamlit.<br>
El repositorio cuenta con los siguientes archivos y carpetas que componen la aplicacion del Dashboard:
* classes: contiene el archivo classes.py donde se define una clase que permite generar pestañas para diferentes "hojas" en el Dashboard.
* ftx_api: contiene el archivo connect.py con el cual se realizan las conecciones a la API de FTX. Dentro se definen funciones para obtener datos del mercado de criptomonedas.
* images: esta carpeta contiene las imagenes usadas en el Dashboard.
* models: esta carpeta contiene dos archivos, cada cual corresponde a las "hojas" del Dashboard. Se crearon dos hojas, una con los graficos de los datos y otra con la calculadora.<br>

Decidí basar el analisis en las 10 monedas que poseen la mayor capitalizacion del mercado (segun la pagina  coinmarketcap.com) y que se encuentren en la plataforma de FTX. Estas son:
* BTC (Bitcoin)
* ETH(Ethereum)
* USDT (Tether)
* BNB (BNB)
* XRP (XRP)
* SOL (Solana) 
* DOGE (Dogecoin)
* DOT (Polkadot)
* Dai (DAI)
* MATIC (Polygon)