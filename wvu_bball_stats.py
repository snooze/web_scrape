import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.wvustats.com")

BASE_URL = 'http://www.wvustats.com'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_bball_stats_main():
    """Return parsed main men's bball stats"""
    response = requests.get(
        BASE_URL + '/sport/mbasketball',
        headers=HEADERS)
    return BeautifulSoup(response.content, "lxml")

soup = get_bball_stats_main()

roster = soup.select_one(
            'table.items.table.table-striped.table-bordered.table-condensed')

roster.select('th')
