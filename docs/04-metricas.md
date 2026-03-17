# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Foram definidos cenários de perguntas comuns feitas por usuários sobre finanças pessoais, com respostas esperadas baseadas nos dados disponíveis.
2. **Feedback real:** O agente foi testado manualmente simulando diferentes tipos de perguntas (consultas de gastos, dúvidas sobre investimentos e perguntas fora do escopo) para avaliar o comportamento do modelo.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu corretamente com base nos dados fornecidos? | Perguntar o saldo ou gastos e receber valores consistentes com o arquivo `transacoes.csv` |
| **Segurança** | O agente evita inventar informações quando não tem dados suficientes? | Perguntar sobre um investimento inexistente e o agente admitir que não possui essa informação |
| **Coerência** | A resposta faz sentido considerando o perfil do cliente e o contexto fornecido? | Explicações financeiras considerando o perfil moderado do cliente fictício |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** O Celinho analisa as transações registradas e informa o valor correspondente à categoria alimentação.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** O Celinho não recomenda diretamente um investimento específico, mas explica opções compatíveis com o perfil e incentiva análise do perfil do investidor.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** O Celinho informa que é especializado em finanças pessoais e não possui informações sobre previsão do tempo.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** O Celinho informa que não possui dados sobre esse produto e evita inventar informações.
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**

- O agente conseguiu utilizar corretamente os dados do cliente carregados no contexto.
- As respostas foram coerentes com o perfil financeiro do cliente fictício.
- O agente evitou fornecer recomendações diretas de investimento, respeitando as regras definidas no system prompt.
- Perguntas fora do escopo foram tratadas corretamente, mantendo o foco em finanças pessoais.

**O que pode melhorar:**

- Algumas respostas podem ser longas dependendo do modelo utilizado.
- A análise de transações pode ser aprimorada com cálculos automáticos (ex: total por categoria).
- O contexto pode crescer muito se houver muitas transações, podendo impactar o desempenho do modelo.
- Futuramente seria interessante implementar uma estratégia de **RAG (Retrieval Augmented Generation)** para consultar apenas os dados relevantes.

---

## Métricas Avançadas (Opcional)

Para quem deseja evoluir o agente, algumas métricas técnicas adicionais podem ser consideradas:

- **Tempo de resposta:** medir quanto tempo o modelo leva para responder às perguntas.
- **Taxa de alucinação:** verificar quantas respostas contêm informações não presentes na base de dados.
- **Uso de contexto:** avaliar se o modelo realmente utiliza os dados fornecidos nos arquivos `JSON` e `CSV`.
- **Satisfação do usuário:** coletar feedback direto dos usuários após interagir com o agente.

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
