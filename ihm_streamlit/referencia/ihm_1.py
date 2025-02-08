import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go
import plotly.express as px

from random import random
from datetime import datetime


def gerar_grafico_temperatura(temp_atual, temp_anterior, temp_placeholder):
    
    graph_indicator = go.Indicator(
        domain={
            'x':[0, 1],
            'y': [0, 1]
        },
        title={
            'text': 'Temperatura (ºC)'
        },
        value=temp_atual,
        mode='gauge + number + delta',
        delta={
            'reference': temp_anterior
        },
        gauge={
            'axis': {
                'range': [0, 100]
            }
        }
    )
    
    figura = go.Figure(graph_indicator)
    
    temp_placeholder.write(figura)


def gerar_grafico_linha_tempo(df, graph_placeholder):
    
    figura = px.line(
        df, 
        x='Hora',
        y='Temperatura (°C)',
        title='Temperatura vs Hora'
    )
    
    graph_placeholder.write(figura)
    

if __name__ == '__main__':
    
    st.set_page_config(
        page_icon=':thermometer:',
        page_title='Protótipo IHM',
        layout='wide'
    )
    
    temperatura_placeholder = st.empty()
    grafico_linha_placeholder = st.empty()
    
    dataframe = pd.DataFrame(
        data = [], 
        columns=['Hora','Temperatura (°C)']
    )
    
    i = 0
    
    temperatura_anterior = 0
    
    while i < 500: 
        
        hora = datetime.now()
        
        hora = hora.strftime('%H:%M:%S')
        
        temperatura = random() * (100 - 10) + 10
        
        dataframe.loc[i, 'Hora'] = hora
        
        dataframe.loc[i, 'Temperatura (°C)'] = temperatura
        
        gerar_grafico_temperatura(temperatura, temperatura_anterior, 
                                  temperatura_placeholder)
        
        gerar_grafico_linha_tempo(dataframe, grafico_linha_placeholder)
        
        time.sleep(10)
        
        i += 1
        
        temperatura_anterior = temperatura
