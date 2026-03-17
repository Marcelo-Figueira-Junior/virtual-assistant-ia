# Passo a passo de execução

## Setup do Ollama 

```bash
# 1. Instalar Ollama (ollama.com)

# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit/Gradio)

```

## Código completo

Todo o código fonte que está no "app.py"

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run ./src/app.py
```
