import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import dataset

from make_data import gap 

#set fig size
plt.rcParams['figure.figsize'] = [10, 7]

#create scatterplot Life Expectancy vs GDP Per Capita (log)
plt.figure()
sns.scatterplot(data = gap, x = "lifeExp", y = "gdpPercap", hue = "continent").set(
    title="Life Expectancy vs GDP Per Capita (log)",
    ylabel = "GDP per Capita (log scale)",
    xlabel = "Life Expectancy")
plt.yscale("log")

plt.savefig("figs/GDP_scatter_log.jpg")


#create scatterplot Life Expectancy vs GDP Per Capita (linear)
plt.figure()
sns.scatterplot(data = gap, x = "lifeExp", y = "gdpPercap", hue = "continent").set(
    title="Life Expectancy vs GDP Per Capita",
    ylabel = "GDP per Capita",
    xlabel = "Life Expectancy")

#labeling outliers
for i in range(gap.shape[0]):
    if gap.gdpPercap[i] > 50000:
        plt.text(x=gap.lifeExp[i]+0.3,y=gap.gdpPercap[i]+0.3,s=(gap.country[i], gap.year[i]))
        
plt.savefig("figs/GDP_scatter.jpg")