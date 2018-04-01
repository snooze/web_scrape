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
        players.append({
            'number': player_number,
            'player name': player_name
        })
    return players
