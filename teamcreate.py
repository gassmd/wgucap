from selenium import webdriver
from hashmap import HashMap
#from excel_populate import get_data

from team import Team
import time
import re
from openpyxl import *

wb = load_workbook("C:/Users/Mike G/Documents/bet/wgucapfin.xlsx")
ws = wb["Sheet1"]

driver = webdriver.Firefox() #creates initial webdriver with firefox
action = webdriver.ActionChains(driver)

team_map = HashMap(33)

name_col = 10
lastseason_col = 11
last10_col = 12
elo_col = 13


def add_teams():                        #adds teams to created hashmap
    for i in range(1, 31):
        team_add = team_create(i)
        team_map.add(i, team_add)

def team_create(current_row):           #creates team object by pulling from excel data
    try:
        team_name = get_data(current_row, name_col)
        last_season = get_data(current_row, lastseason_col)
        last10 = get_data(current_row, last10_col)
        elo = get_data(current_row, elo_col)
        print([team_name, last_season, last10, elo])
        team_obj = Team(team_name, last_season, last10, elo)
        return team_obj
    except TypeError:
        print('type error')

def get_team_map():
    return team_map

def get_data(row_index, col_index):         #returns excel cell data given row and column
    c = ws.cell(row_index, col_index)
    value = c.value
    return value


add_teams()
