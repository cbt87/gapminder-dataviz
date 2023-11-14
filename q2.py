#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#import dataset

from make_data import gap 

sns.set_style('white')

#create facetgrid Time Evolution of Life Expectancy by Continent
g = sns.FacetGrid(gap, col="continent", col_wrap = 3, height = 5, sharex=False)
g.map_dataframe(sns.boxplot, x = "year", y = "lifeExp")

#set title
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Time Evolution of Life Expectancy by Continent', fontsize=15)

#save fig
plt.savefig("figs/lifeExp_overtime_box_by_continent.jpg")