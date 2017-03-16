import requests
from bs4 import BeautifulSoup
from dateutil import parser as dateparser

SOURCE_URL = 'http://www.nuforc.org/webreports/ndxe201702.html'


def extract_ufo(row):
    cells = row.select('td')
    #url = cells[0].select('a')[0].attrs['href']
    d = {}
    d['location'] = cells[1].text + ', ' + cells[2].text
    d['shape'] = cells[3].text
    d['summary'] =  cells[5].text

    try:
        d['date'] = dateparser.parse(cells[0].text)
    except ValueError:
        d['date'] = cells[0].text

    return d

def get_ufos():
    resp =  requests.get(SOURCE_URL)
    txt = ''.join(resp.text.splitlines()[20:])
    soup = BeautifulSoup(txt, 'lxml')
    rows = soup.select('tr')[1:]

    ufolist = []

    for row in rows:
        ufolist.append(extract_ufo(row))
    return ufolist
