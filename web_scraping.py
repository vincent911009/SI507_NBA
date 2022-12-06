from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

years = list(range(1992,2023))

#####################################
### Scrape regular stats ############
#####################################
player_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"
driver = webdriver.Chrome()

for year in years:
    url = player_stats_url.format(year)
    driver.get(url)
    driver.execute_script("window.scrollTo(1,10000)")
    time.sleep(2)
    
    with open("player/{}.html".format(year), "w+", encoding="utf_8_sig") as f:
        f.write(driver.page_source)

dfs = []

for year in years:
    with open("player/{}.html".format(year), encoding="utf_8_sig") as f:
        page = f.read()
    
    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='thead').decompose()
    player_table = soup.find_all(id='per_game_stats')[0]
    player_df = pd.read_html(str(player_table))[0]
    player_df["Year"] = year
    dfs.append(player_df)
    
players = pd.concat(dfs)

players.head()

players.to_csv("players.csv")

#####################################
### Scrape advanced stats ###########
#####################################
player_advanced_stat_url = "https://www.basketball-reference.com/leagues/NBA_{}_advanced.html"

dfs = []

for year in years:
    with open("advanced/{}.html".format(year), encoding="utf_8_sig") as f:
        page = f.read()
    
    soup = BeautifulSoup(page, 'html.parser')
    soup.find('tr', class_='thead').decompose()
    player_table = soup.find_all(id='advanced_stats')[0]
    player_df = pd.read_html(str(player_table))[0]
    player_df["Year"] = year
    dfs.append(player_df)
    
players = pd.concat(dfs)

players.head()

players.to_csv("advanced_data.csv")
