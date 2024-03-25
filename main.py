from get_data import get_data
from data_preprocessing import data_preprocessing

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

xyz = data_preprocessing().create_document().create_embedding()
