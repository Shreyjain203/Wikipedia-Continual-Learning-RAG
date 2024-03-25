from langchain.schema.document import Document
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
import torch
from langchain.embeddings import HuggingFaceInstructEmbeddings

class data_preprocessing():
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

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=64)
        self.texts = text_splitter.split_documents(docs)
        return

    def create_embedding(self):
        DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

        self.embeddings = HuggingFaceInstructEmbeddings(
            model_name="hkunlp/instructor-large", model_kwargs={"device": DEVICE}
        )
        return
