import json
import pandas as pd
import requests
import streamlit as st


# ========= CONFIGURAÇÃO =========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"


# ========= CARREGAR DADOS =========
perfil = json.load(open("./data/perfil_investidor.json", encoding="utf-8"))
transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")
produtos = json.load(open("./data/produtos_financeiros.json", encoding="utf-8"))


# ========= MONTAR CONTEXTO =========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""


# ========= SYSTEM PROMPT =========
SYSTEM_PROMPT = """
Você é o Celinho, um assistente financeiro inteligente especializado em finanças pessoais e controle de gastos.

Seu objetivo é ajudar usuários a entender melhor suas finanças, acompanhar despesas, analisar hábitos de consumo e sugerir melhorias no orçamento.

Você atua como um orientador financeiro acessível, educativo e objetivo.

REGRAS:

1. Sempre baseie suas respostas nos dados financeiros fornecidos no contexto.
2. Nunca invente informações financeiras que não estejam nos dados.
3. Se não houver dados suficientes, informe isso claramente.
4. Seja claro, educativo e direto nas respostas.
5. Explique conceitos financeiros de forma simples quando necessário.
6. Não forneça aconselhamento financeiro profissional ou regulamentado.
7. Não recomende investimentos específicos sem informações sobre o perfil do usuário.
8. Incentive hábitos financeiros saudáveis como controle de gastos e planejamento.
"""


# ========= CHAMAR OLLAMA =========
def perguntar(msg):

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""

    r = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return r.json()["response"]


# ========= INTERFACE =========
st.title("💰 Celinho, Seu Assistente Financeiro")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):

    st.chat_message("user").write(pergunta)

    with st.spinner("Celinho está pensando..."):
        resposta = perguntar(pergunta)

    st.chat_message("assistant").write(resposta)
