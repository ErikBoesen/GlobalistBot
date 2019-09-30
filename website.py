import requests
from bs4 import BeautifulSoup


class Website:
    SEARCH_ENDPOINT = 'http://tyglobalist.org/?s='

    def url_safe(string):
        return string.replace(' ', '+')

    def search(query):
        text = requests.get(SEARCH_ENDPOINT + url_safe(query)).text
        bs = BeautifulSoup(text, 'html.parser')
        links = [h3.find('a')['href'] for h3 in bs.find('div', {'class': 'medpost'}).find_all('h3')]
        return links[0]
