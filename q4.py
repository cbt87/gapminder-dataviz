import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from scipy import stats

#import dataset

from make_data import gap 
from make_data import Africa


plt.figure()
plt.rcParams['figure.figsize'] = [10, 7]
fig, ax = plt.subplots()

#setting up normal distribution based on life expectancy data
mean = gap["lifeExp"].mean()
std = gap["lifeExp"].std()
x = np.linspace(mean-3*std, mean+3*std, 200)
p = stats.norm.pdf(x, mean, std)

# create figure PDF of life expectancy compared to normal distribution
sns.histplot(data = gap, x = "lifeExp", ax = ax, binwidth = 1, kde = True, stat="density", label = "Histogram")
ax.plot(x, p, c="crimson", label='Normal Distribution')
ax.get_lines()[0].set_label("KDE")
ax.set_xlabel("Life Expectancy")
ax.set_title("PDF of life expectancy compared to normal distribution")
ax.legend()


plt.savefig("figs/PDF_life_expectancy.jpg")


#create  figure PDF of life expectancy compared to normal distribution for African countries
plt.figure()
fig, ax = plt.subplots()

#setting up normal distribution based on life expectancy in Africa
mean = Africa["lifeExp"].mean()
std = Africa["lifeExp"].std()
x = np.linspace(mean-3*std, mean+3*std, 200)
p = stats.norm.pdf(x, mean, std)


sns.histplot(data = Africa, x = "lifeExp", ax = ax, binwidth = 1, kde = True, stat="density", label = "Histogram")
ax.plot(x, p, c="crimson", label='Normal Distribution')
ax.get_lines()[0].set_label("KDE")
ax.set_xlabel("Life Expectancy")
ax.set_title("PDF of life expectancy in Africa compared to normal distribution")
ax.legend()

plt.savefig("figs/PDF_life_expectancy_Africa.jpg")