import pandas as pd

gap = pd.read_table("https://raw.githubusercontent.com/jennybc/gapminder/main/inst/extdata/gapminder.tsv")

Africa = gap[gap["continent"] == "Africa"].copy()
