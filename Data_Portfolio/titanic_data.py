import pandas as pd
import numpy as np
import matplotlib.pylab as plt

#Read file
df = pd.read_csv("titanic_data.csv")
#titanic_data.csv is a data set containing information of all of the titainic passengers

#Cleans data set by removing rows missing values
dfTitanic = df.dropna(subset=['Survived', 'Pclass', 'Age', 'Sex'])


#computes fraction of survivors according to class and gender.
males1 = dfTitanic.loc[(dfTitanic['Sex']== 'male') & (dfTitanic['Survived'] > 0) & (dfTitanic['Pclass'] == 1),]  
females1 = dfTitanic.loc[(dfTitanic['Sex']== 'female') & (dfTitanic['Survived'] > 0)  & (dfTitanic['Pclass'] == 1),]

males2 = dfTitanic.loc[(dfTitanic['Sex']== 'male') & (dfTitanic['Survived'] > 0) & (dfTitanic['Pclass'] == 2),]  
females2 = dfTitanic.loc[(dfTitanic['Sex']== 'female') & (dfTitanic['Survived'] > 0)  & (dfTitanic['Pclass'] == 2),]

males3 = dfTitanic.loc[(dfTitanic['Sex']== 'male') & (dfTitanic['Survived'] > 0) & (dfTitanic['Pclass'] == 3),]  
females3 = dfTitanic.loc[(dfTitanic['Sex']== 'female') & (dfTitanic['Survived'] > 0)  & (dfTitanic['Pclass'] == 3),]


class1 = dfTitanic.loc[(dfTitanic['Pclass']== 1) & dfTitanic['Survived'] > 0,]
class2 = dfTitanic.loc[(dfTitanic['Pclass']== 2) & dfTitanic['Survived'] > 0]
class3 = dfTitanic.loc[(dfTitanic['Pclass']== 3) & dfTitanic['Survived'] > 0]

m1 = len(males1)/len(class1)
print("(male class 1 suvivors)/(class 1 survivors) = ", m1)
f1 = len(females1)/len(class1)
print("(female class 1 suvivors)/(class 1 survivors) = ", f1)

print("\n")

m2 = len(males2)/len(class2)
print("(male class 2 suvivors)/(class 2 survivors) = ", m2)
f2 = len(females2)/len(class2)
print("(female class 2 suvivors)/(class 2 survivors) = ", f2)

print("\n")

m3 = len(males3)/len(class3)
print("(male class 3 suvivors)/(class 3 survivors) = ", m3)
f3 = len(females3)/len(class3)
print("(female class 3 suvivors)/(class 3 survivors) = ", f3)




#Creates a histogram of the distribution of passengers who survived vs. passengers who did not survive
my_bins = range(0,85,5)
fig, ax = plt.subplots(figsize=(8,4))

dfTitanic.loc[dfTitanic["Survived"]==1].hist(column="Age", ax=ax, facecolor = "coral", edgecolor="white",alpha=0.6, bins=my_bins)
dfTitanic.loc[dfTitanic["Survived"]==0].hist(column="Age", ax=ax, facecolor = "seagreen", edgecolor="white",alpha=0.5, bins=my_bins)
ax.set_title("Distribution of Age", fontsize=16)
ax.set_xlabel("Age(years)", fontsize=16)
ax.set_ylabel("Frequency", fontsize=16)
ax.legend(["Survived","Dead"])
ax.set_axisbelow(True)
plt.show()

