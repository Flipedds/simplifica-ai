import streamlit as st
from openai import OpenAI
import os

def call_openai_chat_model(prompt):
    client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{prompt}",
        }
    ],
    model="gpt-3.5-turbo")

    return f"{chat.choices[0].message.content}"

st.title("Simplifica.ai")

tab1, tab2 = st.tabs(["Termo Técnico", "Tecnologia"])

with tab1:
    st.header("Simplificação de Termos Técnicos")

    with st.form(key="simplifica_termo_form"):
        nome_termo = st.text_input("Nome do termo técnico", "")
        contexto = st.selectbox("Contexto", ["programação", "design", "negócios", "jogos"])
        nivel = st.selectbox("Nível de Conhecimento", ["básico", "intermediário", "avançado"])

        submit_button_termo = st.form_submit_button(label="Simplificar Termo")

    if submit_button_termo:
        if not nome_termo:
            st.toast("O campo: Nome do termo técnico não pode estar vazio.", icon="⚠️")
        else:
            prompt_termo = f"Explique o termo técnico {nome_termo} para uma pessoa com conhecimento {nivel} em {contexto}."
            resposta_termo = call_openai_chat_model(prompt_termo)
            st.write(resposta_termo)

with tab2:
    st.header("Simplificação de Tecnologia")

    with st.form(key="simplifica_tech_form"):
        nome_tech = st.text_input("Nome da tecnologia", "")

        submit_button_tech = st.form_submit_button(label="Simplificar Tecnologia")

    if submit_button_tech:
        if not nome_tech:
            st.toast("O campo: Nome da tecnologia não pode estar vazio.", icon="⚠️")
        else:
            prompt_tech = f"Explique a tecnologia {nome_tech} de forma simplificada."
            resposta_tech = call_openai_chat_model(prompt_tech)
            st.write(resposta_tech)