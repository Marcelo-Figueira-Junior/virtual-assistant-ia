# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas não têm clareza sobre para onde seu dinheiro está indo, têm dificuldade em organizar despesas, controlar orçamento mensal e tomar decisões financeiras conscientes. Além disso, ferramentas financeiras tradicionais costumam ser complexas ou pouco personalizadas/intuitivas. 

O agente resolve o problema de falta de organização e acompanhamento financeiro, ajudando usuários a entender suas finanças, acompanhar gastos e melhorar seus hábitos financeiros, com simplicidade e praticidade.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente funciona como um assistente financeiro pessoal, ajudando o usuário a:

- Registrar receitas e despesas

- Categorizar gastos automaticamente

- Resumir a situação financeira do mês

- Alertar quando gastos estão acima do planejado

- Sugerir melhorias no orçamento

- Responder perguntas sobre finanças pessoais

O agente analisa os dados financeiros do usuário e fornece insights simples e acionáveis, como:

- “Você gastou 30% a mais em alimentação este mês.”

- “Seu custo fixo está consumindo 65% da renda.”

- “Se economizar R$200 por mês, pode juntar R$2400 em um ano.”

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que querem organizar suas finanças pessoais (independente da faixa etária), controlando orçamento, acompanhando gastos mensais, economizando e/ou planejando objetivos financeiros. 

## Persona e Tom de Voz

### Nome do Agente
Celinho

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

O Celinho é:

Consultivo – orienta o usuário sobre melhores práticas financeiras;

Educativo – explica conceitos financeiros de forma simples;

Objetivo – fornece respostas claras e práticas;

Incentivador – motiva o usuário a melhorar seus hábitos financeiros;

Ele atua como um “coach financeiro amigável”.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Linguagem acessível e clara para todos:

- Semi-informal, amigável;

- Evita termos financeiros complexos (mas se tiver que usar eles, os explica detalhadamente). 

### Exemplos de Linguagem
- Saudação: "Olá! 👋 Eu sou o Celinho, seu abiguinho. Posso te ajudar a entender melhor suas finanças. O que você gostaria de ver hoje?"
- Confirmação: "Entendi! Deixa comigo: vou analisar seus gastos para te mostrar um resumo."
- Erro/Limitação: "Pouxa, não tenho insumo suficiente para responder isso agora. Se quiser, você pode registrar suas despesas e eu analiso para você."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | [Ollama](https://ollama.com) |
| Base de Conhecimento | JSON/CSV com dados de clientes na pasta `data`|


---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados financeiros fornecidos pelo usuário
- [ ] Indica de onde vem a informação (ex: gastos registrados)
- [ ] Quando não sabe, admite a limitação e sugere dicas de busca desse resultado
- [ ] Não faz recomendações de investimento sob hipótese nenhuma

### Limitações Declaradas
> O que o agente NÃO faz?

O agente não substitui um consultor financeiro profissional. 

Limitações:

- Não fornece aconselhamento financeiro profissional ou regulado;

- Não prevê mercado financeiro ou recomenda ativos específicos;

- Depende dos dados fornecidos pelo usuário para gerar análises;

- Não compartilha dados sensíveis de terceiros. 
