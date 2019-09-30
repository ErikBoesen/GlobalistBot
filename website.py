import requests
from bs4 import BeautifulSoup


class Website:
    SEARCH_ENDPOINT = 'http://tyglobalist.org/?s='

    def url_safe(self, string):
        return string.replace(' ', '+')

    def search(self, query):
        text = requests.get(self.SEARCH_ENDPOINT + self.url_safe(query)).text
        bs = BeautifulSoup(text, 'html.parser')
        column = bs.find('ul', {'class': 'medpost'})
        if column is None:
            return 'No results found.'
        links = [h3.find('a')['href'] for h3 in column.find_all('h3')]
        return links[0]
