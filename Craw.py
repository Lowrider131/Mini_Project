from bs4 import BeautifulSoup
import requests

url = "https://shopping.google.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
