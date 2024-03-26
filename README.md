
# Wikipedia-Continual-Learning-RAG
## Description
This project utilizes data extracted from Wikipedia to build a Retriever-Aware Generation (RAG) model. The data extraction is handled by `get_data.py`, which downloads data from Wikipedia and saves it as a text file. The extracted data is then preprocessed into vectors using `data_preprocessing.py`. The project utilizes `memory.py` for ConversationBufferMemory, `prompt.py` for generating proper prompts, and `pipeline.py` for creating and linking the model pipeline. Finally, everything is integrated into `main.py`, where the RAG model is built. When a user asks a question, the model provides an answer. If the model is unable to answer, it uses `get_data.py` to fetch more information and fine-tunes itself before providing an appropriate answer.

## Model Description

## Installation
<ol><li>Clone the repository: `git clone https://github.com/shreyjain203/Wikipedia-Continual-Learning-RAG.git`</li>
<li>Install the required packages: `pip install -r requirements.txt`</li></ol>

## Usage
<ol><li>Run get_data.py to download data from Wikipedia and save it as a text file.</li>
<li>Run data_preprocessing.py to preprocess the data into vectors.</li>
<li>Run main.py to build the RAG model and interact with it.</li></ol>

## Contributors
<ul><li>Shrey Jain</li></ul>
