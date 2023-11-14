#import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#import dataset

from make_data import gap 

sns.set_style('white')

#create facetgrid for Distribution of Life Expectancy by Continent
g = sns.FacetGrid(gap, col="continent",col_wrap = 3, height = 4)
g.map_dataframe(sns.histplot, x="lifeExp", binwidth = 1)

#set title and axis label
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Distribution of Life Expectancy by Continent', fontsize=15)
g.set_xlabels("Life Expectancy")

#save fig
plt.savefig("figs/lifeExp_hist_by_continent.jpg")