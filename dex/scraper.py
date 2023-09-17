from bs4 import BeautifulSoup #pip install beautifulsoup4
import requests #pip install requests

def scrape():
    url = "https://pokemondb.net/pokedex/1"
    page = requests.get(url) #load page
    soup = BeautifulSoup(page.content, 'html.parser') #makes the page readable/writable
    name_class = soup.find(class_="main-content grid-container")
    name = name_class.find("h1").text.strip()
    print(name)
    #for i in range(1, 1010):
        #page = requests.get(url) #load page
        #soup = BeautifulSoup(page.content, 'html.parser') #makes the page readable/writable
scrape()




