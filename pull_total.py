from flask import Flask, render_template
from datetime import datetime
from bs4 import BeautifulSoup
import requests


def get_var():
    url = "https://smashrun.com/jonamerica/overview"
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')


    result = soup.find('div', { "class" : "data distance-text" })


    return result.text.upper()




print(get_var())
