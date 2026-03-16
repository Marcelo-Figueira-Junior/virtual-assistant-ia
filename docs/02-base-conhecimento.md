# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|--------|--------|----------------------|
| `transacoes.csv` | CSV | Armazena o histórico de receitas e despesas do usuário para análise financeira |
| `categorias_gastos.json` | JSON | Define categorias de gastos (alimentação, transporte, lazer, etc.) para classificação das despesas |
| `perfil_usuario.json` | JSON | Contém informações básicas do usuário como renda mensal, objetivos financeiros e limites de orçamento |
| `historico_interacoes.csv` | CSV | Registra interações anteriores com o agente para manter contexto e personalizar respostas |

---

# Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram adaptados para representar cenários realistas de finanças pessoais. Foram incluídas categorias de gastos mais comuns (como alimentação, transporte, moradia e lazer) e exemplos de transações mensais para simular o comportamento financeiro de um usuário típico.

Também foram adicionados campos como:

- **categoria da despesa**
- **tipo de transação (receita ou despesa)**
- **data da transação**
- **valor da transação**

Essas adaptações permitem que o agente faça análises mais úteis, como identificar padrões de gastos, calcular totais mensais e gerar insights financeiros.

---

# Estratégia de Integração

## Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da sessão do agente. Os dados são lidos pelo backend (ex: Python) e armazenados em estruturas de dados que podem ser consultadas durante a conversa.

Quando o usuário faz uma pergunta sobre suas finanças, o agente consulta os dados relevantes (como transações ou perfil financeiro) antes de gerar a resposta.

---

## Como os dados são usados no prompt?

> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são **consultados dinamicamente** antes de cada resposta do agente.

O fluxo funciona da seguinte forma:

1. O usuário envia uma pergunta.
2. O sistema identifica quais dados são relevantes (ex: transações recentes ou saldo).
3. Esses dados são formatados como contexto.
4. O contexto é incluído no **prompt enviado ao modelo de linguagem**.

Isso garante que o agente responda com base nas informações reais disponíveis e reduz o risco de respostas inventadas.

---

# Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```text
Dados do Cliente:
- Nome: João Silva
- Renda mensal: R$ 4.500
- Objetivo financeiro: economizar para viagem
- Orçamento mensal: R$ 3.500

Resumo do mês atual:
- Total gasto: R$ 2.150
- Total recebido: R$ 4.500
- Saldo atual: R$ 2.350

Últimas transações:
- 02/11: Supermercado - R$ 320
- 04/11: Uber - R$ 45
- 06/11: Streaming - R$ 39
- 08/11: Restaurante - R$ 120
- 10/11: Academia - R$ 90

Categorias mais utilizadas:
- Alimentação: R$ 780
- Transporte: R$ 210
- Lazer: R$ 260
```
