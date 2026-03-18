<h1 align="center">🤖 Celinho — Agente Financeiro Inteligente</h1>

<p align="center">

<img src="https://img.shields.io/badge/Python-Programming-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge">

</p>

<p align="center">
🇧🇷 <a href="#pt-br">Português</a> | 🇺🇸 <a href="#en">English</a>
</p>

---

# 🇧🇷 Português

<h2 id="pt-br"></h2>

## 📖 Sobre o Projeto

**Celinho** é um **agente financeiro inteligente** desenvolvido para auxiliar usuários na análise de suas finanças e no planejamento de decisões financeiras.

O agente funciona como um **assistente financeiro virtual**, analisando dados do usuário e fornecendo orientações baseadas em seu perfil e histórico financeiro.

Este projeto foi desenvolvido como parte de um **desafio prático de aplicação de IA no setor financeiro**.

---

## 🎯 Caso de Uso

O **Celinho** atua como um assistente financeiro capaz de:

* 📊 analisar transações financeiras
* 💰 sugerir estratégias de investimento
* 📉 identificar padrões de gastos
* 🎯 auxiliar no planejamento de metas financeiras

Seu objetivo é ajudar usuários a **entender melhor suas finanças e tomar decisões mais informadas**.

---

## 🧠 Funcionamento do Agente

Fluxo simplificado do sistema:

```text
Usuário → Chatbot (Celinho) → Modelo LLM local (Ollama)
                    ↓
            Base de Conhecimento
   (transações, perfil, produtos financeiros)
                    ↓
         Resposta financeira personalizada
```

Etapas principais:

1. O usuário conversa com o **Celinho** através da interface do chatbot
2. O sistema consulta a **base de dados do cliente**
3. O modelo executado localmente via **Ollama** analisa o contexto
4. O agente gera uma **resposta personalizada baseada nos dados disponíveis**

---

## 📚 Base de Conhecimento

O **Celinho** utiliza dados estruturados para gerar respostas contextualizadas.

Arquivos utilizados:

| Arquivo                   | Formato | Descrição                        |
| ------------------------- | ------- | -------------------------------- |
| transacoes.csv            | CSV     | Histórico de transações          |
| historico_atendimento.csv | CSV     | Interações anteriores            |
| perfil_investidor.json    | JSON    | Perfil e preferências do cliente |
| produtos_financeiros.json | JSON    | Produtos financeiros disponíveis |

Esses dados permitem que o agente **entenda o contexto financeiro do usuário**.

---

## 🧪 Avaliação do Agente

A qualidade das respostas pode ser avaliada com base em:

* 🎯 precisão das respostas
* 📊 coerência com o perfil do cliente
* 📉 utilidade das recomendações financeiras
* 🤝 relevância das respostas para o contexto do usuário

---

## 💻 Tecnologias Utilizadas

* Python
* Streamlit
* Ollama

---

## 📁 Estrutura do Projeto

```bash
lab-agente-financeiro/
│
├── README.md
│
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── src/
│   └── app.py
│
├── assets/
│
└── examples/
```

---

## 🚀 Como executar o projeto

### Pré-requisitos

Antes de executar o projeto instale:

* Python 3.x
* Ollama
* pip

---

### Clonar o repositório

```bash
git clone SEU_REPOSITORIO
```

---

### Instalar dependências

```bash
pip install -r requirements.txt
```

---

### Executar o agente

```bash
streamlit run src/app.py
```

---

# 🇺🇸 English

<h2 id="en"></h2>

## 📖 About the Project

**Celinho** is an **intelligent financial agent** designed to assist users in analyzing their finances and planning financial decisions.

The system works as a **virtual financial assistant**, analyzing user data and providing suggestions based on financial history and profile.

This project was developed as part of a **practical challenge involving AI applications in the financial sector**.

---

## 🎯 Use Case

Celinho acts as a **financial assistant** capable of:

* analyzing financial transactions
* suggesting investment strategies
* identifying spending patterns
* helping users plan financial goals

---

## 🧠 Agent Workflow

System workflow:

```
User → Chatbot (Celinho) → Local LLM via Ollama
                  ↓
           Knowledge Base
(transactions, profile, financial products)
                  ↓
        Personalized financial response
```

---

## 📚 Knowledge Base

Celinho uses structured data sources:

| File                      | Format | Description                  |
| ------------------------- | ------ | ---------------------------- |
| transacoes.csv            | CSV    | Transaction history          |
| historico_atendimento.csv | CSV    | Previous interactions        |
| perfil_investidor.json    | JSON   | Investor profile             |
| produtos_financeiros.json | JSON   | Available financial products |

---

## 💻 Technologies Used

* Python
* Streamlit
* Ollama

---

## 🚀 Running the Project

### Prerequisites

Before running the project install:

* Python 3.x
* Ollama
* pip

---

### Clone the repository

```bash
git clone YOUR_REPOSITORY
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run the application

```bash
streamlit run src/app.py
```

---

<p align="center">
⭐ If you found this project interesting, consider giving it a star!
</p>
