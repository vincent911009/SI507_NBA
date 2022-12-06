from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

players = pd.read_csv("players.csv")

del players["Unnamed: 0"]
del players["Rk"]
# print(players.head())
players["Player"] = players["Player"].str.replace("*", "", regex=False)

def single_row(df):
    if df.shape[0]==1:
        return df
    else:
        row = df[df["Tm"] == "TOT"]
        row["Tm"] = df.iloc[-1,:]["Tm"]
        return row
        
players = players.groupby(["Player", "Year"]).apply(single_row)

players.index = players.index.droplevel()
players.index = players.index.droplevel()
players[players["Player"] == "Greg Anderson"]


advanced = pd.read_csv("advanced_data.csv")

del advanced["Unnamed: 0"]
del advanced["Unnamed: 19"]
del advanced["Unnamed: 24"]
del advanced["Rk"]
# print(players.head())
advanced["Player"] = advanced["Player"].str.replace("*", "", regex=False)
advanced = advanced.groupby(["Player", "Year"]).apply(single_row)
advanced.index = advanced.index.droplevel()
advanced.index = advanced.index.droplevel()
advanced[advanced["Player"] == "Greg Anderson"]

combined = players.merge(advanced, how="outer", on=["Player", "Year"])

combined.to_csv("Combined_stats.csv")