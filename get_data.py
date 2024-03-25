# !pip install wikipedia

import wikipedia


class get_data:
    def __init__(self, text):
        self.text = text
        
    def find_title_list(self):
        return wikipedia.search(
            self.text,
            results=5
            )
        
    def get_data(self, title):
        #find the data
        data = wikipedia.page(title).content
        return data
