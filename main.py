from flask import Flask, render_template
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from multiprocessing import Value #for counter

counter = Value('i', 0)

app = Flask('Plash_Custom')

@app.route('/')

def index():
    with counter.get_lock():
        counter.value += 1
    if (counter.value % 2) == 0:
        return render_template('index.html', variable=get_yearly(), sizing=get_size(get_yearly()))
    else:
        return render_template('index.html', variable=get_total(), sizing=get_size(get_total()))

def get_size(variable):
    length = len(variable)
    print(length)
    if length > 35:
        print("Returning small")
        return "small_VW"
    elif length > 28:
        print("Returning medium")
        return "medium_VW"
    elif length > 20:
        print("Returning large")
        return "large_VW"
    else:
        print("Returning xlarge")
        return "xlarge_VW"

def get_yearly():
    url = "https://smashrun.com/jonamerica/overview/2020"
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    result = soup.find('div', { "class" : "data distance-text" })

    return result.text.upper()

def get_total():
    url = "https://smashrun.com/jonamerica/overview"
    headers = requests.utils.default_headers()
    headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    result = soup.find('div', { "class" : "data distance-text" })

    return result.text.upper()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
