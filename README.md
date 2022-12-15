# SI507 Final Project: NBA Players & Teams Relationship and Stats Observation

This program is a SI 507 final project designed to find the relationship between players and teams and also have some stats analysis. After implementing the interactive code, user can get some sense of whether relationship between players or stats analysis.

Main Tools: Python

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install selenium.

```bash
pip install selenium

```
User also need to download the latest web browser driver. In this project, I use chromedriver.

## Data Source

The data comes from:

[Basketball Reference](https://www.basketball-reference.com/)

## Getting Start

You need to scrape the html from [Basketball Reference](https://www.basketball-reference.com/) by using selenium and the code is in the file called "web_scraping.ipynb". Then, you can get two csv files called "players.csv" & "advanced_data.csv". 

Then, doing data processing by using "Data_processing.ipynb", you can get the combined csv called "Combined_stats.csv".

Next, store team and players columns data and save as "Player_team_graph.csv".

## Main.py
Now, we can enter into main.py. In the main code, we construct a graph structure between players and teams.

In this light, we can run the code. We have two games can play. 

1. Find the shortest path from nba player A to nba player B, and also find the average shortest path of all nba players to whom you want.

2. There are 4 different kinds of index you can view.

- Compare one stats and choose numbers of players for an entire NBA history.
- Compare one stats and choose numbers of players for a specific year.
- View one stats and remain the highest for an entire NBA history.
- Compare one stats and choose numbers of players for an entire NBA history, but first eliminate players who are not satisfy the first requirement.

If you want to play game1, type 1, otherwise type 2 to play game2. Or you don't want to play, you can type anything other than 1 and 2. 

## Data Presentation

- Game 1: Show the shortest path from player A to player B and show the shortest average path to one player

- Game 2: A bar chart showing the different stat for a limit numbers of players in different index.
     - Compare one stats and choose numbers of players for an entire NBA history.
        - Type the stat you want to compare.
        - Type the number of players you want to remain.
     - Compare one stats and choose numbers of players for a specific year.
        - Type the stat you want to compare.
        - Type the number of players you want to remain.
        - Type a specific year you want to compare (only can compare year from 1992-2022).
3
     - View one stats and remain the highest for an entire NBA history.
        - Choose one stat, which is the highest from 1992-2022 you want to view.
     - Compare one stats and choose numbers of players for an entire NBA history, but first eliminate players
who are not satisfy the first requirement.
        - Type the stat you want to let it becomes the minimum criterion stat.
        - Type the numbers of players you want to remain as threshold.
        - Type the final stat you want to compare.
        - Type the numbers of players you want to remain at last.
In
## Built With

[Python3](https://www.python.org/downloads/) - The programming language on the back end

Packages:
 - BeautifulSoup - scrape webpage
 - selenium - fetch data from webpage
 - pandas - store data into csv
 - matplotlib.pyplot - visualize data
 - collections - use defaultdict

## Authors

- Wen-Kai Chung
