import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('wvu_stats', backend='sqlite', expire_after=7200)

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


def get_player_table_headers(table):
    cols = []
    for th in roster.select('th'):
        cols.append({'name': th.text})
    return cols

get_player_table_headers(roster)

def get_player_main_info(table):
    cols = get_player_table_headers(table)
    players = []
    for row in table.select('tr')[1:-1]:
        player_number = int(row.select_one('td').text)
        player_name = row.select('td')[1].text
        player_pos = row.select('td')[2].text
        player_ht = row.select('td')[3].text
        player_wt = row.select('td')[4].text
        player_class = row.select('td')[5].text
        player_hometown = row.select('td')[6].text
        for player in row.select('td')[1]:
            href = player.attrs['href']
        players.append({
            'number': player_number,
            'name': player_name,
            'height': player_ht,
            'weight': player_wt,
            'class': player_class,
            'hometown': player_hometown,
            'bio_link': player.attrs['href']
        })
    return players

player_main_info = get_player_main_info(roster)
