# Final Project Progress May 16

import pandas as pd
import numpy as np

# Data Input
master = pd.read_csv('master.csv', header=0, encoding='latin-1') 
people = pd.read_csv('people1.csv', header = 0, encoding='latin-1')

teams = pd.read_csv('teams.csv', header = 0)

result = pd.merge(master, people, on = 'bref_id')

for colname in result.columns.values:
    if '_y' in colname:
        result = result.drop(columns = colname) # Drop extra columns


# Team Info
import csv
with open('teams.csv', mode='r') as infile:
    reader = csv.reader(infile)
    abrev = {rows[0]:rows[1] for rows in reader}
    del abrev['ï»¿team'] # For some reason, the top row of the csv gets entered this way




# Tools to access Spotrac, store information
from collections import defaultdict as dd
import requests
from bs4 import BeautifulSoup



"""Takes year, team name, returns soup of that injury webpage"""
def get_injury_page(year, team):

    # https://www.spotrac.com/mlb/disabled-list/2015/cumulative-player/new-york-yankees/
    # Example URL

    year = str(year)

    team = team.replace(" ","-").lower()
    team = team.replace(".","").lower()

    url = "https://www.spotrac.com/mlb/disabled-list/" + year + "/cumulative-player/" + team

    response = requests.get(url)   # request the page

    if response.status_code == 404:                 # page not found
        print("There was a problem with getting the page:")
        print(player_url)
        return 'error'

    data_from_url = response.text                   # the HTML text from the page
    soup = BeautifulSoup(data_from_url,"lxml")      # parsed with Beautiful Soup
    return soup        



""" Takes soup, scrapes information and returns dataframe"""


# Lets us work with datetime objects regarding time spent on IL
from datetime import date
from datetime import datetime


def get_pl_injury_info(soup): 

    AllDivs = soup.findAll('tr', 'parent')

    year = int(soup.findAll('option',selected=True)[0].getText())

    df = pd.DataFrame(columns= ["player_name", "position", "current_org", "injury_type", "time_on_IL", "cash_on_IL", "injury_year", "IL_start", "IL_end"])

    i = 0

    for entry in AllDivs:

        name_chunk = entry.findAll('td','player')


        if "\n" in name_chunk[0].getText():

            name_chunk = str(name_chunk)

            info_chunk = entry.findAll('td','center')

            # Get name string

            player_name = name_chunk.split('>')[2].split('<')[0] # Unwieldy, but works

            # Get player info

            position = info_chunk[0].getText()

            current_org = info_chunk[1].getText()

            injury_type = info_chunk[2].getText()

            time_on_IL = info_chunk[5].getText() # Still a character string

            cash_on_IL = info_chunk[6].getText() # Get rid of $ and commas maybe?


            # Get date info

            date_chunks = info_chunk[4].findAll('span')
            for j in range(1,len(date_chunks)):
                
                date_to_date = date_chunks[j].getText()
                
                
                start_date = date_to_date.split(' ')[0]
                end_date = date_to_date.split(' ')[2]
                try:
                    IL_start = datetime.strptime(start_date, '%m/%d')
                    IL_start = IL_start.replace(year = year)

                    IL_end = datetime.strptime(end_date, '%m/%d')
                    IL_end = IL_end.replace(year = year)
                except ValueError:
                    IL_start = datetime.strptime(start_date, '%m/%d')
                    IL_start = IL_start.replace(year = year)                    

                    IL_end = 'Currently on IL'
                    



                row = [player_name, position, current_org, injury_type, time_on_IL, cash_on_IL, year, IL_start, IL_end]

                df.loc[i] = row
                i += 1
        else:
            continue

    return df

""" Get injury DataFrames for each season"""
injury_df = pd.DataFrame()

for team in teams['team']:
    for year in [2015,2016,2017,2018,2019]:
        
        #time.sleep(2) # Can be used to make sure you don't pester spotrac with too many requests

        page_soup = get_injury_page(year,team)   

        df = get_pl_injury_info(page_soup)

        df['injury_org'] = pd.Series(team, index = df.index)

        injury_df = injury_df.append(df, ignore_index = True)


"""Synthesizing data for analysis"""

# Currently commented out, but allows for mmerging into 1 final dataframe


"""
master_df = result

newdf = pd.DataFrame(columns = ['mlb_name', 'injury2015_2019'])

for x in range(0,len(result)):
    name = result.iloc[x]['mlb_name']

    if name in injury_df['player_name_full'].values:
        
        t = pd.DataFrame({"mlb_name":[name],
                          "injury2015_2019":[1]})
        
        newdf = newdf.append(t)
    else:
        t = pd.DataFrame({"mlb_name":[name],
                          "injury2015_2019":[0]})

        newdf = newdf.append(t)
    
master_df = pd.merge(master_df, newdf, on = 'mlb_name')
"""


''' Export files code '''

# Export your injury data frame
# export_csv = injury_df.to_csv(r"C:\Users\USERNAME&DIRECTORY\NAME_OFDF", index = None, header=True)


