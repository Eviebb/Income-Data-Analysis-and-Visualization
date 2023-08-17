# import libraries
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# import data as data frame
data = pd.read_csv(r"C:\Users\Lorie\OneDrive\Desktop\Projects\US Income Table Project Data Analysis\Income.csv")

# establish values from data set
income_group_pop_data = data.loc[:,"income_group_population"]
total_pop_all_income_data = data.loc[:,"total_population_all_income_groups"]
state_name_data = data.loc[:, "state_name"]

# finds column values of income group by state
state_name_uv = data['state_name'].unique()

for mean_income_values in data:



# scatterplot
income_scatterplot = plt.scatter(income_group_pop_data, total_pop_all_income_data, c="#023020", marker="d", alpha=0.3)
#plt.show()

# bar graph
#income_by_state = plt.bar(state_name_uv, income_group_pop_data)
