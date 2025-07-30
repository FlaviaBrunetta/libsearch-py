
# 📚 Buscador Inteligente de Livros

libsearch-py foi desenvolvido com base no workshop "Aprenda Modelos de Consulta Preditiva criando um recomendador de livros com IA generativa" durante o Sprint IA Generativa da Progra{m}aria


## 🚀 Objetivos

Criar um buscador inteligente de livros capaz de interpretar comandos como:

“Quero um romance curto!”

“Me dê mais informações sobre tal livro!”

E retornar resultados relevantes usando IA e o protocolo MCP.

## ⚒️ Etapas

1. Filtragem Inteligente de Livros – Carol Silva (Neuralmed)
Explicação sobre o dataset utilizado.

Implementação de uma função Python com filtros por:

Gênero do livro.

Número de páginas.

Avaliação (rating).

Retorno dos 10 melhores livros com base nos critérios.

Introdução ao MCP (Model Context Protocol):

Padrão aberto criado pela Anthropic.

Facilita a integração entre IA e ferramentas externas.

Estrutura modular e reutilizável.

Benefícios do MCP na construção de soluções escaláveis.

2. Expansão do MCP com Agentes de IA – Jéssica dos Santos (Winnin)
Revisão da primeira parte.

Introdução ao LangGraph:

Biblioteca para criação de agentes de IA via grafos.

Gerencia o fluxo de integração entre ferramentas.

Adição de nova funcionalidade ao buscador:

Consultar informações detalhadas sobre um livro específico.

Implementação de memória para:

Permitir ao buscador responder com base em perguntas anteriores.

Resolução de erros e ajustes no processo.

## 💻 Stack utilizada

Python

Dataset "GoodReads" - kaggle - https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k

MCP (Model Context Protocol)

LangGraph

## 📋 Pré-requisitos e Configurações

### 1. Baixar o arquivo do GoodReads
Baixar o csv no link: [Kaggle - GoodReads 100k books](https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k/data)

### 2. Conta OpenAI e Chave API

Para utilizar o sistema de chat com IA, você precisará de uma chave da OpenAI.

### 3. Conta Apify (Opcional)

Para acessar dados atualizados do Goodreads, você pode criar uma conta gratuita na Apify.

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
OPENAI_API_KEY=sua_chave_openai_aqui
APIFY_API_KEY=sua_chave_apify_aqui_opcional
```


## 🏷️ Etiquetas

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

