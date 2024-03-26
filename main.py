# !pip install nltk

from get_data import get_data
from data_preprocessing import data_preprocessing
from prompt import get_prompt_template
from memory import memory
from pipeline import pipeline

import nltk
from langchain.chains import ConversationalRetrievalChain

def training():
    db = data_preprocessing().create_document().create_embedding()
    prompt = get_prompt_template()
    memory = memory()
    llm = pipeline()
    return db, prompt, memory, llm

training_flag = True
need_user_input_flag = True

while True:
    if training_flag:
        db, prompt, memory, llm = training()
        training_flag = False

    if need_user_input_flag:
        user_prompt = input("Enter the prompt")

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 1}),
        get_chat_history=lambda o:o,
        memory=memory,
        combine_docs_chain_kwargs={'prompt': prompt})

    result = qa_chain(user_prompt)
    if result['answer'] == "I don't know":
        print("""
              Currently, our model doesn't know the answer
              and retraining itself to get better results.
              Please wait for few more minutes""")
        
        training_flag = True
        need_user_input_flag = False

        nouns = []
        for word,pos in nltk.pos_tag(nltk.word_tokenize(str(user_prompt))):
                if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                    nouns.append(word)

        for noun in nouns:
            wikipedia_obj = get_data(noun)
            relevant_titles = wikipedia_obj.find_title_list()
            print(relevant_titles)

            # Finding the most relevant title
            # Right now, we're using the first title
            title = relevant_titles[0]

            data = wikipedia_obj.get_data(title)

            with open(f'data/{title}.txt', 'w') as file:
                file.write(data)
