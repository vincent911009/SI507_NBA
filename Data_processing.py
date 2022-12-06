from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests
# from bs4 import BeautifulSoup

player_stats_url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

# # url = player_stats_url.format(1991)
# # data = requests.get(url)
# # with open("player/1991.html", "w+") as f:
# #     f.write(data.text)
    
# # driver = webdriver.Chrome()
# # year = 1991
# # url = player_stats_url.format(year)

# # driver.get(url)
# # driver.execute_script("windows.scrollTo(1,10000)")
# # time.sleep(2)

# # html = driver.page_source

# # with open("player/{}.html".format(year), "w+") as f:
# #     f.write(html)
    
    
# years = list(range(1991,1992))    
# # for year in years:
# url = player_stats_url.format(2002)
# driver = webdriver.Chrome()
# driver.get(url)
# driver.execute_script("window.scrollTo(1,10000)")
    # time.sleep(2)
    # html = driver.page_source
    # with open("player/{}.html".format(year), "w+", encoding="utf_8_sig") as f:
    #     f.write(html)
        
# dfs = []
# for year in years:
#     with open("player/{}.html".format(year), encoding="utf_8_sig") as f:
#         page = f.read()
        
#     soup = BeautifulSoup(page, "html.parser")
#     soup.find('tr', class_="over_header").decompose()
#     player_table = soup.find_all(id="per_game_stats")[0]
#     player_df = pd.read_html(str(player_table))[0]
#     player_df["Year"] = year
#     dfs.append(player_df)
        
        


options = Options()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)
action = ActionChains(driver)


url = player_stats_url.format(2002)
# player = requests.get(url)
# with open("player/{}.html".format(year), "w+", encoding="utf_8_sig") as f:
#     f.write(html)
driver.get(url)
Login_Btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='pxc-fn-login']/a")))

action.move_to_element(Login_Btn).click().perform()
