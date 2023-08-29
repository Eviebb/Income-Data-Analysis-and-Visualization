# import libraries
import pandas as pd
from matplotlib import pyplot as plt

# import data as data frame
data = pd.read_csv(r"C:\Users\Lorie\OneDrive\Desktop\Projects\US Income Table Project Data Analysis\Income.csv")

# define unique column values for bar graph
bar_graph_grouping_population_with_DC = data.groupby('state_name', as_index=True)['total_population_all_income_groups'].mean()
final_bar_graph_grouping_population = bar_graph_grouping_population_with_DC.drop("District of Columbia", axis='index')

# bar graph showing sample size recorded in data by all 50 states (excludes District of Columbia)
plt.style.use('fivethirtyeight')
income_bar_graph = final_bar_graph_grouping_population.plot(kind='barh', title='Total Population By State',
                                           ylabel='Total Population of All Income Groups', xlabel='State Name',
                                           figsize=(60, 60))
plt.gcf().subplots_adjust(left=0.164, bottom=0.071, right=0.938, top=0.955)
plt.show()