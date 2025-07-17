import streamlit as st
import json

st.set_page_config(layout="wide")
st.title("🎬 Luma AI - Visualizador de Gerações")

# Carrega os dados
with open("lista.json", "r") as f:
    dados = json.load(f)

# Filtros
modelos = sorted(set(item["model"] for item in dados if item["model"]))
modelo_selecionado = st.sidebar.selectbox("Filtrar por modelo", ["Todos"] + modelos)

fotos = sorted(set(item["image_url"] for item in dados if item["image_url"]))
foto_selecionada = st.sidebar.selectbox("Filtrar por imagem inicial", ["Todos"] + fotos)

# Aplica os filtros
filtrados = dados
if modelo_selecionado != "Todos":
    filtrados = [d for d in filtrados if d["model"] == modelo_selecionado]

if foto_selecionada != "Todos":
    filtrados = [d for d in filtrados if d["image_url"] == foto_selecionada]

# Exibe os resultados
for item in filtrados:
    st.markdown("---")
    cols = st.columns([1, 1.2])  # reduzido
    with cols[0]:
        if item["image_url"]:
            st.image(item["image_url"], caption="Imagem de entrada", use_container_width=True)
        else:
            st.warning("Sem imagem de entrada")
        st.markdown(f"**Modelo:** `{item['model']}`")
        st.markdown(f"**Data:** `{item['created_at']}`")
    with cols[1]:
        st.video(item["video_url"])
        st.markdown(f"**Prompt:** _{item['prompt']}_")
