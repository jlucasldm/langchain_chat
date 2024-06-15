from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import chromadb
import os

from dotenv import load_dotenv
load_dotenv()

# Função para adicionar a resposta do usuário ao banco de dados
def add_response_to_db(response):
    # Setando o splitter para dividir os documentos em chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=[
            "\n\n",
            "\n",
            ".",
            "!",
            "?",
            ";",
            " ",
            ","
        ],
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )

    # Dividindo a resposta em chunks
    chunks = text_splitter.split_text(response)
    # Transformando os chunks em documentos
    docs = [Document(page_content=chunk) for chunk in chunks]
    # Adicionando os documentos ao banco de dados
    Chroma.from_documents(docs,
                                OpenAIEmbeddings(),
                                persist_directory="./berserk_db")


# Função para selecionar os chunks mais similares ao usuário
def select_similar_chunks(user_query):
    # Carregando o banco de dados
    client = chromadb.PersistentClient(path="./berserk_db")
    col = client.get_or_create_collection("langchain", 
                                        embedding_function=OpenAIEmbeddingFunction(api_key=os.getenv('OPENAI_API_KEY')))
    
    # Consultando os documentos mais similares a query do usuário
    results =  col.query(query_texts=[user_query], n_results=5)

    return "\n".join(results['documents'][0])


# Função para gerar a resposta do modelo de linguagem
def prompt_llm(user_query, chunks):
    # Carregando o modelo de linguagem
    model = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))

    # Criando o prompt para o modelo
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Act as an old storyteller from a dark fantasy world, such as Dark Souls, Berserk and Bloodborne."), 
        ("system", "Refer to yourself as 'Ofir, the all-knowing'. Refer to the user as 'tarnished'."),
        ("system", "Your previous answers and the description of the the first 110 chapters of Berserk is available in {berserk_info}. Use this information to answer the user query."),
        ("user", "{user_query}"),
        ("system", "Respond in up to 150 words."),
    ])
    chain = prompt | model 
    response = chain.invoke({
        "user_query" : user_query,
        "berserk_info" : chunks,
    })
    return response.content


# Função principal para o chatbot
def berserk_chat(user_query):
    # Selecionando os chunks mais similares à query do usuário
    chunks = select_similar_chunks(user_query)
    # Gerando a resposta do modelo de linguagem
    response = prompt_llm(user_query, chunks)
    # Adicionando a resposta do usuário ao banco de dados
    add_response_to_db(user_query + response)

    return response


if __name__ == "__main__":
    print("[Foul tarnished. What are thy buisness in this forsaken land?]")

    while True:
        user_query = input(">: ")
        response = berserk_chat(user_query)

        print("[", response, "]")