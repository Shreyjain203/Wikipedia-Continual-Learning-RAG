
# Wikipedia-Continual-Learning-RAG
## Description
This project utilizes data extracted from Wikipedia to build a Retriever-Aware Generation (RAG) model. The data extraction is handled by `get_data.py`, which downloads data from Wikipedia and saves it as a text file. The extracted data is then preprocessed into vectors using `data_preprocessing.py`. The project utilizes `memory.py` for ConversationBufferMemory, `prompt.py` for generating proper prompts, and `pipeline.py` for creating and linking the model pipeline. Finally, everything is integrated into `main.py`, where the RAG model is built. When a user asks a question, the model provides an answer. If the model is unable to answer, it uses `get_data.py` to fetch more information and fine-tunes itself before providing an appropriate answer.

## Model Description
Still working on it.

## Installation
1. Clone the repository: `git clone https://github.com/shreyjain203/Wikipedia-Continual-Learning-RAG.git`
2. Install the required packages: `pip install -r requirements.txt`

## Usage
1. Run `get_data.py` to download data from Wikipedia and save it as a text file.
2. Run `data_preprocessing.py` to preprocess the data into vectors.
3. Run `main.py` to build the RAG model and interact with it.

## Contributors
<ul><li>Shrey Jain</li></ul>
