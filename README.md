
# Wikipedia-Continual-Learning-RAG
## Description
This project utilizes data extracted from Wikipedia to build a Retriever-Aware Generation (RAG) model. The data extraction is handled by `get_data.py`, which downloads data from Wikipedia and saves it as a text file. The extracted data is then preprocessed into vectors using `data_preprocessing.py`. The project utilizes `memory.py` for ConversationBufferMemory, `prompt.py` for generating proper prompts, and `pipeline.py` for creating and linking the model pipeline. Finally, everything is integrated into `main.py`, where the RAG model is built. When a user asks a question, the model provides an answer. If the model is unable to answer, it uses `get_data.py` to fetch more information and fine-tunes itself before providing an appropriate answer.

## Implementation Details
#### 1. TheBloke/Llama-2-13B-chat-GPTQ Model (LLM)
This implementation utilizes TheBloke as the Large Language Model to generate human-like, coherent responses based on the retrieved documents.

#### 2. SentenceTransformers (Langchain(Chroma) Model)
SentenceTransformers is used to create embeddings for the sentences, enabling efficient and semantic similarity search among them. Chroma pretrained model was used as it had the best performance.

#### 3. langchain (Data Ingestion, Vectorization, and Storage)
Langchain is employed for ingesting and vectorizing the dataset and for storing the vectorized representations of the data.

## Installation
1. Clone the repository: `git clone https://github.com/shreyjain203/Wikipedia-Continual-Learning-RAG.git`
2. Install the required packages: `pip install -r requirements.txt`

## Usage
Run `main.py` to build the RAG model and interact with it.

## Contributors
<ul><li>Shrey Jain (Me)</li></ul>
