from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader

from dotenv import load_dotenv
load_dotenv()

def create_berserk_db():
    # Carregando todos os documentos dos volumes de Berserk
    # e transformando-os em uma lista de strings com seus conteúdos
    loader = DirectoryLoader('./berserk', loader_cls=TextLoader)
    documents = loader.load()
    documents = [doc.page_content for doc in documents]

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
            ",",
        ],
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )

    # Dividindo os documentos em chunks 
    chunks = text_splitter.split_text("\n".join(documents))

    # Transformando os chunks em documentos
    docs = [Document(page_content=chunk) for chunk in chunks]

    # Criando o banco de dados e inserindo os documentos 
    # com seus respectivos embeddings 
    db = Chroma.from_documents(docs,
                                OpenAIEmbeddings(),
                                persist_directory="./berserk_db")
    return db

if __name__ == "__main__":
    create_berserk_db()
    print("Banco de dados criado com sucesso!")