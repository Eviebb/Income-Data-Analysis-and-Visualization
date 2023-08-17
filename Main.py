# import libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# import data as data frame
data = pd.read_csv(r"C:\Users\Lorie\OneDrive\Desktop\Projects\US Income Table Project Data Analysis\Income.csv")

# establish values from data set
income_group_pop_data = data.loc[:, "income_group_population"]
total_pop_all_income_data = data.loc[:, "total_population_all_income_groups"]
state_name_data = data.loc[:, "state_name"]

# define unique column values for bar graph
state_name_uv = data['state_name'].unique()
bar_graph_grouping = data.groupby('state_name', as_index=False)['total_population_all_income_groups'].mean()

# scatterplot
#income_scatterplot = plt.scatter(income_group_pop_data, total_pop_all_income_data, c="#023020", marker="d", alpha=0.3)

# bar graph
plt.style.use('fivethirtyeight')
income_bar_graph = bar_graph_grouping.plot(kind='barh', title='Total Population By State',
                                           ylabel='Total Population of All Income Groups', xlabel='State Name',
                                           figsize=(20, 10))
plt.show()
