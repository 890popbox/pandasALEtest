#Chris Antes, Life exp Analysis

import numpy as np
import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as plt

#Import the csv and re-name column properly
csv_path = 'healthy-life-expectancy-and-years-lived-with-disability.csv'
df = pd.read_csv(csv_path)
df = df.rename(columns={'Entity' : 'Location'})

#Hold years 1990 to 2016 and avg life exp globally
_yrs = []
_ahle = []

#What is the average life expentacy overall?
#Let's go through 1990 to 2016..
for i in range(0, 27):
    yr = df.loc[df['Year'] == 1990+i] #Gather all countries at this current year, print the average life exp age
    hle = float("{:.2f}".format(yr['Healthy Life Expectancy (IHME)'].sum() / yr['Healthy Life Expectancy (IHME)'].count())) #Formatting the decimal two places
    _yrs.append(1990+i), _ahle.append(hle) #Append to two lists at once

#Hold the country code and the country itself
code = df["Code"].unique().tolist()
country = df["Location"].unique().tolist()

ahle_ls = [] #Hold average life exp for 1990-2016 in a specific location


#Does location affect life expentacy? 1990 to 2016 life exp per location
for c in country:
    place = df.loc[df['Location'] == c] #Only return the rows if it is part of that country and then print the average life exp
    hle = float("{:.2f}".format(place['Healthy Life Expectancy (IHME)'].sum() / place['Healthy Life Expectancy (IHME)'].count())) #Formatting the decimal two places
    ahle_ls.append(hle) #Append to one list
    
#Has life expentacy improved overtime? and why?
#Yes, due to more wide spread health information over the years and world development 

#Life expentacy 1990-2016 per location
fig1 = pd.DataFrame({"average life exp": ahle_ls},
                    index=country)

fig1 = fig1.sort_values(by='average life exp', ascending=True)
fig1.plot(title='Life expentacy 1990-2016, per location', kind="bar",align='center', width=1, figsize=(50, 10))

#Life expentacy 1990-2016 global avg
fig2 = pd.DataFrame({"average life exp": _ahle},
                    index=_yrs)
#fig2 = fig2.sort_values(by='years'), It's already sorted by years as the index
fig2.plot(title='Life expentacy 1990-2016, global avg', kind="line")

#Describing the dataframe to get the lowest life exp, highest, and information on how disablity affects it.
df.describe()

