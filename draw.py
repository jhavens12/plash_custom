from PIL import Image, ImageDraw, ImageFont
import requests
from bs4 import BeautifulSoup
import credentials

import_png = True
local_dir = credentials.local_dir

H = 2436
W = 1125

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

def get_size(variable):
    length = len(variable)
    if length > 35:
        print("Returning small")
        return 45
    elif length > 28:
        print("Returning medium")
        return 50
    elif length > 20:
        print("Returning large")
        return 70
    else:
        print("Returning xlarge")
        return 90

msg = get_yearly()
if import_png:
    im  = Image.open(local_dir+"grey.png")
else:
    im = Image.new("RGBA",(W,H),"black")

fnt = ImageFont.truetype(local_dir+'Fonts/Finador-Light.ttf', get_size(msg))
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg, font=fnt)
draw.text(((W-w)/2,(H-h)/2), msg, font=fnt, fill="white")
im.save(local_dir+'Yearly.png')

msg = get_total()
if import_png:
    im  = Image.open(local_dir+"grey.png")
else:
    im = Image.new("RGBA",(W,H),"black")
fnt = ImageFont.truetype(local_dir+'Fonts/Finador-Light.ttf', get_size(msg))
draw = ImageDraw.Draw(im)
w, h = draw.textsize(msg, font=fnt)
draw.text(((W-w)/2,(H-h)/2), msg, font=fnt, fill="white")
im.save(local_dir+'Total.png')
