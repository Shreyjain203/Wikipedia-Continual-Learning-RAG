from get_data import get_data
from data_preprocessing import data_preprocessing
from prompt import get_prompt_template
from memory import memory


db = data_preprocessing().create_document().create_embedding()
prompt = get_prompt_template()
memory = memory()


if 1==0:  # If my answer is not good enough and need more data
    wikipedia_obj = get_data("Lucknow Super Giants")
    relevant_titles = wikipedia_obj.find_title_list()
    print(relevant_titles)

    # Finding the most relevant title
    # Right now, we're using the first title
    title = relevant_titles[0]

    data = wikipedia_obj.get_data(title)

    with open(f'data/{title}.txt', 'w') as file:
        file.write(data)
