import pandas as pd
import numpy as np
import matplotlib.pylab as plt

#Liam Carney


filepath = 'weather_data.csv'
#weather_data.csv is a data set of the monthly levels of precipitation for the last 100 years in Boulder CO.


df = pd.read_csv(filepath)
df = df.replace(to_replace = "Tr", value = 0)

#Creates boxplot of precipitation based on season
df = df.astype(float)
seasonGroups = {'DEC':'Winter', 'JAN':'WINTER', 'FEB':'WINTER', 'MAR':'SPRING', 'APR':'SPRING', 'MAY':'SPRING'
              , 'JUN':'SUMMER', 'JUL':'SUMMER', 'AUG':'SUMMER', 'SEP':'FALL', 'OCT':'FALL', 'NOV':'FALL'}

fig, ax = plt.subplots(figsize=(10,5))
groupType = df.set_index('Year')
dfGrouped = groupType.astype(float)
dfGrouped = dfGrouped.groupby(seasonGroups, axis = 1).mean()
ax.set_title("Level of Precipitation per Season", fontsize=16)
ax.set_xlabel("Seasons", fontsize=16)
ax.set_ylabel("Precipitation (inches)", fontsize=16)
dfGrouped.boxplot()
plt.show()


#creates histogram of the amount of precipitation during september for the last 100 years.
fig, ax = plt.subplots(figsize = (8,4))
sP = df.loc[:, 'SEP']
sP = sP.astype(float)
sP.hist(density = True, ax=ax)
#marks the outlier (SEPT 2013) in red
ax.patches[9].set_fc('r')
ax.grid(alpha=.25)
ax.set_title("September Precipitation", fontsize=15)
ax.set_xlabel("Amount of Precipitation", fontsize=10)
ax.set_ylabel("Frequency", fontsize=10)
plt.show()

#calculates 5 Number Sumarry for Septemebers precipitation
print("September's Mean Precipitation: ", sP.mean())
print("Standard deviation for September's Precipitation: ", sP.std())

turkey = np.percentile(sP, [0, 25, 50, 75, 100], interpolation = 'midpoint')
print("Turkey 5 number summary: \n Minimum = {}\n Median= {}\n Maximum = {}".format(*turkey))
