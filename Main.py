# import libraries
import pandas as pd
from matplotlib import pyplot as plt

# import data as data frame
data = pd.read_csv(r"C:\Users\Lorie\OneDrive\Desktop\Projects\US Income Table Project Data Analysis\Income.csv")

# establish column values from data set
income_group_pop_data = data.loc[:, "income_group_population"]
total_pop_all_income_data = data.loc[:, "total_population_all_income_groups"]

# income scatterplot
#income_scatterplot = plt.scatter(income_group_pop_data, total_pop_all_income_data, c="#023020", marker="d", alpha=0.3)

# define unique column values for bar graph
bar_graph_grouping_population = data.groupby('state_name', as_index=True)['total_population_all_income_groups'].mean()

# bar graph showing sample size recorded in data by state
plt.style.use('fivethirtyeight')
#income_bar_graph = bar_graph_grouping_population.plot(kind='barh', title='Total Population By State',
#                                           ylabel='Total Population of All Income Groups', xlabel='State Name',
#                                           figsize=(60, 60))
#plt.gcf().subplots_adjust(left=0.164, bottom=0.071, right=0.938, top=0.955)

# define values for histogram
state_name_groups = data.groupby('state_name')

# income_group_population for rows in District of Columbia
DC_income_group_data = data.query("state_name == 'District of Columbia'")["income_group_population"]

# histogram of the District of Columbia's recorded income groups
#plt.hist(DC_income_group_data, cumulative=True)
plt.show()
