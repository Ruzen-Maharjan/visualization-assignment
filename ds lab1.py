"""
Assignment 1 - Data Visualization
Author : Ruzen Maharjan

This program created three graphs using World Bank Data:
    1. Line plot (GDP over time)
    2. Bar chart (GDP comparison in 2022)
    3. Scatter plot (GDP vs Life Expectancy in 2022)
    
"""
"""

Imports

"""
import pandas as pd
import matplotlib.pyplot as plt

"""
Functions

"""
def plot_line_gdp(df_gdp):
"""
Line plot
This creates a line plot of GDP from 2000 to 2022.
"""

plt.figure()
uk = df_gdp.loc["United Kingdom", "2000" : "2022"]
us = df_gdp.loc["United States", "2000" : "2022"]
germany = df_gdp.loc["Germany", "2000" : "2022"]
india = df_gdp.loc["India", "2000" : "2022"]

plt.plot(uk, label = "United Kingdom")
plt.plot(us, label = "United States")
plt.plot(germany, label = "Germany")
plt.plot(india, label = "India")

plt.title("GDP FROM 2000 TO 2022")
plt.xlabel("Year")
plt.ylabel("GDP IN US$")
plt.legend()
plt.xticks(uk.index[::2])
plt.tight_layout()
plt.savefig("GDP.png")
plt.show()  

def plot_bar_gdp_2022(df_gdp):
"""
Bar Chart
This creates a bar chart comparing GDP in 2022
"""
plt.figure()

values = [
    df_gdp.loc["United Kingdom", "2022"],
    df_gdp.loc["United States", "2022"],
    df_gdp.loc["Germany", "2022"],
    df_gdp.loc["India", "2022"]
      ]
countries = ["United Kingdom", "United States", "Germany", "India"]
plt.bar(countries, values)
plt.title("GDP COMPARISON IN 2022")
plt.ylabel("GDP IN US$")
plt.savefig("comparison.png")
plt.show()

def plot_scatter_gdp_life(df_gdp, df_life):
"""
Scatter plot
This creates a scatter plot of GDP VS LIFE EXPECTANCY in 2022
"""

plt.figure()
uk_gdp = df_gdp.loc["United Kingdom", "2022"]
us_gdp = df_gdp.loc["United States", "2022"]
germany_gdp = df_gdp.loc["Germany", "2022"]
india_gdp = df_gdp.loc["India", "2022"]

uk_life = df_life.loc["United Kingdom", "2022"]
us_life = df_life.loc["United States", "2022"]
germany_life = df_life.loc["Germany", "2022"]
india_life = df_life.loc["India", "2022"]

gdp_values = [uk_gdp, us_gdp, germany_gdp, india_gdp]
life_values = [uk_life, us_life, germany_life, india_life]

plt.scatter(gdp_values, life_values, s = 100)
plt.text(uk_gdp, uk_life, "United Kingdom")
plt.text(us_gdp, us_life, "United States")
plt.text(germany_gdp, germany_life, "Germany")
plt.text(india_gdp, india_life, "India")
plt.title("GDP VS LIFE EXPECTANCY IN 2022")
plt.xlabel("GDP IN US$")
plt.ylabel("LIFE EXPECTANCY IN YEARS")
plt.tight_layout()
plt.savefig("scatter.png")
plt.show()

"""
Main program
"""

"""
Read data (Skip first 4 rows using skiprows CSV)
"""
df_gdp = pd.read_csv("gdp.csv", skiprows = 4)
df_life = pd.read_csv("life_expectancy.csv", skiprows = 4) 

"""
Set country name as index
"""

df_gdp = df_gdp.set_index("Country Name")
df_life = df_life.set_index("Country Name")

"""
Call functions
"""
plot_line_gdp(df_gdp)
plot_bar_gdp_2022(df_gdp)
plot_scatter_gdp_life(df_gdp, df_life)



  



