"""
 Program:
    CS241 Assignment 13, Data Analysis Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary:
    This program will take in the values from a csv file
    and display the contents accordingly. It will also
    deal with data manipulation as well as using different
    libraries such as seasborn and pandas to edit the data.            
"""

import pandas as pd # Our data manipulation library
import numpy as np
import seaborn as sns # Used for graphing/plotting
import matplotlib.pyplot as plt # If we need any low level methods
import os # Used to change the directory to the right place


players = pd.read_csv("basketball_players.csv")
#print(players.columns)


master = pd.read_csv("basketball_master.csv")
#print(master.columns)

nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")
#print()
#print()
#print(nba.columns)


#mean = nba["points"].mean()
#median = nba["points"].median()

#print("Points per season: Mean:{:.2f}, Median:{}".format(mean, median))
#print()

#print(nba[["year", "useFirst", "lastName", "points"]].sort_values("points", ascending=False).head(5))


#sns.boxplot(data=nba[["points", "assists", "rebounds"]]).set_title("Total Points, Assists and Rebounds")
#plt.savefig("boxplot_total_points_assists_rebounds.png")
#plt.show()


nba_grouped_year = nba[["points", "year"]].groupby("year").median()
nba_grouped_year = nba_grouped_year.reset_index()
#sns.regplot(data=nba_grouped_year, x="year", y="points").set_title("Median Points Per Year")
#plt.savefig("boxplot_PointsPerSeason.png")
#plt.show()


nba["fgMissed"] = nba["fgAttempted"] - nba["fgMade"]
nba["ftMissed"] = nba["ftAttempted"] - nba["ftMade"]

nba["player_Efficiency_Value"] = ((nba["points"] + nba["rebounds"] + nba["assists"] + nba["steals"] +  nba["blocks"] -
                            nba["fgMissed"] - nba["ftMissed"] - nba["turnovers"]) / nba["GP"])
#print(nba[["year", "useFirst", "lastName", "points", "player_Efficiency_Value"]].sort_values("points", ascending=False).head(10))

#print(nba[["year", "useFirst", "lastName", "rebounds", "assists", "steals", "points"]].sort_values("points", ascending=False).head(50))


#threePoint = nba[["year", "threeAttempted", "threeMade"]].groupby("year").median()
#threePoint.plot()
#plt.show()

#threePoint_melt = threePoint.reset_index().melt("year", var_name="Key", value_name="Three Point Shots(median)")
#sns.lineplot(data=threePoint_melt, x="year", y="Three Point Shots(median)", hue="Key")
#plt.savefig("lineplot_Three_Points_Shots.png")
#plt.show()

nba = nba.groupby(['useFirst', 'lastName']).mean().reset_index()
nba = nba[nba.GP > 0]

nba["points_per_game"] = nba["points"] / nba["GP"]
nba["assists_per_game"] = nba["assists"] / nba["GP"]
nba["steals_per_game"] = nba["steals"] / nba["GP"]
nba["rebounds_per_game"] = nba["rebounds"] / nba["GP"]


#GOAT = nba[["useFirst", "lastName", "points_per_game", "rebounds_per_game", "steals_per_game", "assists_per_game"]]
#GOAT = GOAT.sort_values("points_per_game", ascending = False).head(50)
#pd.set_option('display.expand_frame_repr', False)
#print()
#print(GOAT)


#GOAT = nba[["useFirst", "lastName", "points_per_game", "rebounds_per_game", "steals_per_game", "assists_per_game"]]
#GOAT = GOAT.sort_values("assists_per_game", ascending = False).head(50)
#pd.set_option('display.expand_frame_repr', False)
#print()
#print(GOAT)


#GOAT = nba[["useFirst", "lastName", "points_per_game", "rebounds_per_game", "steals_per_game", "assists_per_game"]]
#GOAT = GOAT.sort_values("steals_per_game", ascending = False).head(50)
#pd.set_option('display.expand_frame_repr', False)
#print()
#print(GOAT)


#GOAT = nba[["useFirst", "lastName", "points_per_game", "rebounds_per_game", "steals_per_game", "assists_per_game"]]
#GOAT = GOAT.sort_values("rebounds_per_game", ascending = False).head(50)
#pd.set_option('display.expand_frame_repr', False)
#print()
#print(GOAT)

master = pd.read_csv("basketball_master.csv")
nba = pd.merge(players, master, how="left", left_on="playerID", right_on="bioID")

nba = nba[nba.GP > 0]
nba["points_per_game"] = nba["points"] / nba["GP"]
nba["assists_per_game"] = nba["assists"] / nba["GP"]
nba["steals_per_game"] = nba["steals"] / nba["GP"]
nba["rebounds_per_game"] = nba["rebounds"] / nba["GP"]

nba["Country"] = nba["birthCountry"]
nba = nba.set_index('Country')
nba = nba.groupby(['Country']).mean()
print(nba)
nba_topCountry_perPoints = nba["points_per_game"].groupby("Country").nlargest(10)
print(nba_topCountry_perPoints)
#nba_topCountry_perPoints = nba_topCountry_perPoints.sort_values("points_per_game", ascending = False).head(6)
#nba_topCountry_median_perPoints = nba_topCountry_perPoints.groupby("birthCountry").median()
#nba_topCountry_perPoints = nba_topCountry_perPoints.reset_index()
#print(nba)
#nba_topCountry_perPoints = nba_topCountry_perPoints[nba_topCountry_perPoints["points_per_game"] > 0]
#sns.regplot(data=nba_topCountry_perPoints, x="birthCountry", y="points_per_game").set_title("Median of Top 6 Country Each Year")
#plt.show()
#nba = pd.nba({'birthCountry': ['USA', 'BRA', 'AUS', 'FRA', 'PUR', 'CAN'], 'points_per_game': }














