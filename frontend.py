import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(page_title="Clima Local", layout="wide")

st.title("Clima Local")

try:
    dados = obter_dados_meteorologicos()

    st.subheader("Indicadores meteorológicos")

    st.metric("Temperatura", f"{dados['temperatura']:.1f} °C")
    st.metric("Umidade relativa", f"{dados['umidade_relativa']:.0f} %")
    st.metric("Sensação térmica", f"{dados['sensacao_termica']:.1f} °C")
    st.metric("Precipitação", f"{dados['precipitacao']:.1f} mm")
    st.metric("Velocidade do vento", f"{dados['velocidade_vento']:.1f} km/h")

    st.caption(f"Horário da consulta: {dados['horario']}")

except Exception as erro:
    st.error(f"Falha ao carregar os dados: {erro}")