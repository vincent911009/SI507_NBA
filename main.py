import csv
import pandas as pd
from collections import defaultdict
import numpy as np
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
        
# Maps players to a dictionary of: name of players
nba_player = defaultdict(set)
# Maps teams to a dictionary of: name of teams
nba_team = defaultdict(set)


def load_data():
    """
    Load Data from player_team_graph and return nba_players, nba_teams as dict[set]
    """
    with open('Player_team_graph.csv', newline='', encoding="UTF-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    new_data = []
    for i in range(int(len(data)/2)):
        res = data[2*i]
        new_data.append(res)

    for x in new_data:
        for i in range(1, len(x)):
            nba_player[x[i]].add(x[0])
            nba_team[x[0]].add(x[i])
    
    return nba_player, nba_team


def shortest_path(player1, players2):
    """
    Returns the shortest list of (nba_player, nba_team) pairs
    that connect the player1 to the player2.
    If no possible path, returns None.
    """
    solution_found = False
    no_solution = False
    solution = list()

    initial = Node(state=player1, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(initial)
    explored = set()
    i = 0
    while solution_found == False:

        if frontier.empty() == True:
            no_solution = True
            solution_found = True
        
        node = frontier.remove()

        if node.state == players2:
            # Return the solution
            solution_found = True
            while node.parent is not None:
                pid, mid = node.state, node.action
                solution.append((mid, pid))
                node = node.parent
            solution.reverse()

        explored.add(node)
        children = neighbors_for_person(node.state)
        for child in children:
            child_node = Node(state=child[1], action=child[0],parent=node)
            frontier.add(child_node)
            if child_node.state == players2:
                # Return the solution
                solution_found = True
                while child_node.parent is not None:
                    pid, mid = child_node.state, child_node.action
                    solution.append((mid, pid))
                    child_node = child_node.parent
                solution.reverse()
    
    if solution_found == True:
        if no_solution == True:
            return None
        return solution


def neighbors_for_person(player):
    """
    Returns (nba_player, nba_team) pairs for players
    who starred with a given player.
    """
    teams = nba_player[player]
    neighbors = set()
    for team in teams:
        for player in nba_team[team]:
            neighbors.add((team, player))
    return neighbors


def main():
    print("Hello, welcome to a NBA game.")
    print("In this program, there are two games you can play.")
    print("1. find the shortest path from nba player A to nba player B, and also find the average shortest path of all nba players to whom you want.")
    print("2. There are 4 different kinds of index you can view. More detail in the game.")
    print("Now, let's go to play the game.")
    
    while True:
        you_choice = input("Enter which game you want to play (If type 1, you will play Game 1. If type 2, you will play Game 2. If type others, you will leave.): ")
        if you_choice == "1":
            load_data()
            print("Load Data.......")
            print("Game 1 started:...........")
            player1 = input("Name of player1(Ex:Kevin Durant): ")
            if player1 is None:
                sys.exit("Person not found.")
            player2 = input("Name of player2(Ex:Russell Westbrook): ")
            if player2 is None:
                sys.exit("Person not found.")

            path = shortest_path(player1, player2)

            if path is None:
                print("Not connected.")
            else:
                degrees = len(path)
                print("There is "f"{degrees} degrees of these two players.")
                path = [(None, player1)] + path
                for i in range(degrees):
                    person1 = path[i][1]
                    person2 = path[i+1][1]
                    team = path[i+1][0]
                    print(f"{i + 1}: The same team {person1} and {person2} stayed in is {team}")
            
            
            anyone = input("Name of play you want to know the average shortest path: ")    
            print(f"Now we want to find the average shortest path of all nba players to {anyone}.")
            print(f"The average {anyone} number of all players is......: ")
            degrees_for_all = []
            
            for player in nba_player:
                if player != anyone:
                    paths = shortest_path(player, anyone)
                    if paths is None:
                        continue
                    degree = len(paths)
                    degrees_for_all.append(degree)
            
            average = (1/len(degrees_for_all)) * sum(degrees_for_all)
            print(average)
            print("Game 1 finished. If you want to play again, please type 1.")
            continue
        
        elif you_choice == "2":
            stats = pd.read_csv("Combined_stats.csv")
            print("Load Data.......")
            print("Game 2 started:..........")
            print("Introduction to game 2. There are 4 different visualization index you can play.")
            print("First, you can find what stats you want to inspect. And below are all the stats you can type: ")
            print("FG%(Field Goal Percentage), 3P%(3 Points Percentage), eFG%(efficient Field Goal Percentage, ")
            print("FT%(Free Throw Percentage), ORB(Offensive Rebound), DRB(Defensive Rebound), TRB(Total Rebound), ")
            print("AST(Assist), STL(Steala), BLK(Block), TOV(Turnover), PF(Personal Foul), PER(Player Efficient Rating), ")
            print("TS%(True Shooting Percentage), 3PAr(3 Point Attempt Rate), FTr(Free Throw Attempt Rate), ORB%(Offensvie Rebound Percentage),")
            print("DRB%(Defensive Rebound Percentage), TRB%(Total Rebound Percentage), AST%(Assist Percentage), STL%(Steal Percentage), ")
            print("BLK%(Block Percentage), TOV%(Turnover Percentage), USG%(Usage Percentage), OWS(Offensive Win Share),")
            print("DWS(Defensive Win Share), WS(Win Share), WS/48(Win Share Per 48), OBPM(Offensive Box Plus/Minus), DBPM(Defensive Box Plus/Minus")
            print("BPM(Box Plus/Minus), VORP(Value over Replacement Player)")
            time.sleep(1)
            print("All above are the stats you can view. And you only have to type the words before parenthesis.")
            print("Now, we have to introduce 4 different index.")
            print("1. Compare one stats and choose numbers of players for an entire NBA history.")
            print("2. Compare one stats and choose numbers of players for a specific year.")
            print("3. View one stats and remain the highest for an entire NBA history.")
            print("4. Compare one stats and choose numbers of players for an entire NBA history, but first eliminate players who are not satisfy the first requirement.")

            yes = input("If you understand the stats and the rule, please type 'yes' and going to the game or you want to leave just type anything: ")

            while True:
                if yes == "yes":
                    choose = input("Choose which index you want to view(type 1 or 2 or 3 or 4) or you want to leave type anything: ")
                    if choose == "1":
                        x = input("Type the stat you want to compare: ")
                        y = int(input("Type the number of players you want to remain: "))
                        highest_scoring = stats[(stats["G_x"] > 70)].sort_values(x, ascending=False).head(y)
                        highest_scoring.plot.bar("Player",x)
                        plt.ylabel(x)
                        plt.tight_layout()
                        plt.show()
                    elif choose == "2":
                        x = input("Type the stat you want to compare: ")
                        y = int(input("Type the number of players you want to remain: "))
                        year = int(input("Type a specific year you want to compare(only can compare year from 1992-2022): "))
                        highest_scoring = stats[(stats["G_x"] > 70) & (stats["Year"] == year)].sort_values(x, ascending=False).head(y)
                        highest_scoring.plot.bar("Player",x)
                        plt.ylabel(x)
                        plt.tight_layout()
                        plt.show()
                    elif choose == "3":
                        y = input("Choose one stat, which is the highest from 1992-2022 you want to view: ")
                        highest_scoring_season = stats.groupby("Year").apply(lambda x: x.sort_values(y, ascending=False).head(1))
                        highest_scoring_season.plot.bar("Year",y)
                        plt.ylabel(y)
                        plt.show()
                    elif choose == "4":
                        x = input("Type the stat you want to let it becomes the minimum criterion stat: ")
                        y = int(input("Type the numbers of players you want to remain as threshold: "))
                        z = input("Type the final stat you want to compare: ")
                        m = int(input("Type the numbers of players you want to remain at last: "))
                        highest_scoring = stats[stats["G_x"] > 70].sort_values(x, ascending=False).head(y)
                        highest_scoring = highest_scoring.sort_values(z, ascending=False).head(m)
                        highest_scoring.plot.bar("Player",z)
                        plt.ylabel(z)
                        plt.tight_layout()
                        plt.show()
                    else:
                        break
                else:
                    break
        else:
            print("Hope you enjoy these games. Thank you.")
            break
    
if __name__ == "__main__":
    main()