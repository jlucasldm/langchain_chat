# Ofir, the all-knowing (Berserk Chatbot)

Ofir é um sábio que viveu durante a Era de Ouro do Bando do Falcão. Ouviu e testemunhou histórias de bravura, traição e sacrifício. Faça perguntas sobre os personagens, a história, e o mundo de Berserk. Ofir está ansioso para compartilhar seu conhecimento com você.

Projeto desenvolvido durante o curso "Criação de aplicações baseadas em LLMs", ofertado pela Universidade Federal da Bahia, ministrado por [Gustavo Pinto](https://github.com/gustavopinto). Chatbot desenvolvido utilizando o modelo GPT-3.5-turbo da OpenAI, refinado sobre as sinopses detalhadas dos volumes 1 ao 109 de Berserk, coletados de um [fórum de fãs](https://berserk.fandom.com/).


## Sobre o projeto

Durante o curso, diversos conceitos de LLM (Large Language Models) foram abordados, bem como a utilização de APIs para interação com esses modelos. As etapas de loading, transforming, embbeding, storing e retrieving foram exploradas e implementadas ao longo do curso, culminando na criação de um chatbot que aplicasse esse conceitos 
utilizando um modelo generativo de texto.

Como projeto final, decidi criar um chatbot que interagisse com o usuário sobre o clássico mangá Berserk. Foram coletadas informações sobre a história em fórums desenvolvidos pelos fãs da obra (até o final do arco Golden Age). Os dados foram carregados, tratados, embedados e armazenados em um banco de dados vetorial e utilizados como referência para a geração de respostas do chatbot. O chatbot armazena o histórico de conversas com o usuário e é capaz de engajar em diálogos sobre o mundo de Berserk de forma coerente e contextualizada com a obra do visionário Kentaro Miura.

Os dados são carregados e processados em chunks utilizando loaders disponibilizados pela biblioteca langchain. Os chunks são embedados utilizando a ferramenta de embedding da OpenAI. A persistência dos chunks e seus embeddings é feita pelo banco de dados vetorial ChromaDB, que permite a indexação e busca de vetores de alta dimensionalidade. O chatbot utiliza a API paga da OpenAI, que disponibiliza o modelo GPT-3.5-turbo, para gerar respostas.

## Como rodar o projeto
É necessário ter o Python 3.8 ou superior instalado. Recomenda-se a utilização de um ambiente virtual para instalar as dependências do projeto.

Para iniciar um ambiente virtual, execute:
```python -m venv venv```
````source venv/bin/activate```

1. Clone o repositório
```git clone```

2. Instale as dependências
```pip install -r requirements.txt```

3. Crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:
```OPENAI_API_KEY=<sua chave de API da OpenAI>```

4. Inicialize o banco de dados vetorial
```python load_berseker_db.py```

5. Rode o chatbot
```python berserk_chat.py```


## Exemplo de uso
>[Foul tarnished. What are thy buisness in this forsaken land?]

>\>: Greetings, Ofir. My name is Maliketh, the black blade. Tell me, who is Guts?

>[Ah, Maliketh, the Black Blade, you seek knowledge of the infamous warrior known as Guts. He is a fierce and relentless swordsman, bearing a tragic past and a cursed destiny. Guts' path is stained with blood and shadow, marked by betrayal and loss. His strength is unmatched, his will unbreakable, as he battles against demons, both within and without. Once a lone mercenary, Guts found himself drawn into the tumultuous world of the Band of the Falcon, led by the enigmatic Griffith. Through countless battles and betrayals, Guts emerged as the Black Swordsman, driven by a singular goal - to seek vengeance against the demonic forces that haunt his existence. His journey is a dark and twisted odyssey, where every step brings him closer to the heart of darkness that consumes his soul.]
	

## Modelo e dataset
O modelo utilizado é o GPT-3.5-turbo, disponibilizado pela OpenAI. O dataset foi coletado manualmente em um [fórum de discussão sobre o mangá Berserk](https://berserk.fandom.com/) e contém informações sobre os personagens, a história e o mundo do mangá até o final do arco Golden Age. Foram coletadas as sinopses detalhadas de todos os capítulos em língua inglesa (do primeiro ao 109º) em documentos de texto e utilizadas como referência para a geração de respostas do chatbot. Os dados estão disponíveis na pasta `berserk`.
