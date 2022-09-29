import streamlit as st
import pandas as pd
from classes.multiapp import MultiApp
from models import grafics, calculator


app = MultiApp()

app.add_app("Graficos", grafics.app)
app.add_app("Calculadora", calculator.app)

app.run()

