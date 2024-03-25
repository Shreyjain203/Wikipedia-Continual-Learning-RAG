# !pip install langchain
# !pip install torch
# !pip install -U langchain-community
# !pip install instructorembedding
# !pip install -U sentence-transformers==2.2.2
# !pip install chromadb

from langchain.schema.document import Document
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
import torch
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import Chroma

class data_preprocessing:
    def __init__(self) -> None:
        pass
        
    def create_document(self):
        directory_path = 'data/'
        docs = []

        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, 'r') as file:
                content = file.read()
                docs.append(Document(page_content = content))

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=5000,
            chunk_overlap=64
            )

        self.texts = text_splitter.split_documents(docs)
        return self

    def create_embedding(self,
                         model_name="hkunlp/instructor-large"):
        DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

        self.embeddings = HuggingFaceInstructEmbeddings(
            model_name=model_name, model_kwargs={"device": DEVICE}
        )
        db = Chroma.from_documents(
            self.texts,
            self.embeddings,
            persist_directory="vector_db"
            )
        return db
