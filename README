# Elden Ring Chatbot
Projeto desenvolvido durante o curso "Criação de aplicações baseadas em LLMs", ofertado pela Universidade Federal da Bahia, ministrado por [Gustavo Pinto](https://github.com/gustavopinto).

Durante o curso, diversos conceitos de LLM (Large Language Models) foram abordados, bem como a utilização de APIs para interação com esses modelos. As etapas de load, transform, embed, store e retrieve foram exploradas e implementadas ao longo do curso, culminando na criação de um chatbot que aplicasse esse conceitos 
utilizando um modelo generativo de texto.

Como projeto final, decidi criar um chatbot que interagisse com o usuário sobre o jogo Elden Ring. Foram coletadas informações sobre a lore do jogo e sobre o gameplay. Os dados foram carregados, tratados, embedados e armazenados em um banco de dados vetorial e utilizados como referência para a geração de respostas do chatbot. O chatbot armazena o histórico de conversas com o usuário e é capaz de responder perguntas sobre o jogo, bem como manter uma conversa casual.

Os dados são carregados e processados em chunks utilizando loaders disponibilizados pela biblioteca langchain. Os chunks são embedados utilizando a ferramenta de embedding da OpenAI. A persistência dos chunks e seus embeddings é feita pelo banco de dados vetorial ChromaDB, que permite a indexação e busca de vetores de alta dimensionalidade. O chatbot utiliza a API paga da OpenAI, que disponibiliza o modelo GPT-4.0, para gerar respostas.


## Como rodar o projeto
É necessário ter o Python 3.8 ou superior instalado. Recomenda-se a utilização de um ambiente virtual para instalar as dependências do projeto.

1. Clone o repositório
```git clone```

2. Instale as dependências
```pip install -r requirements.txt```

3. Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:
```
OPENAI_API_KEY=<sua chave de API da OpenAI>
```