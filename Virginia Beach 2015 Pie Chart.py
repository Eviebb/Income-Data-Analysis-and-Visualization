# import libraries
import pandas as pd
from matplotlib import pyplot as plt

# import data as data frame
data = pd.read_csv(r"C:\Users\Lorie\OneDrive\Desktop\Projects\US Income Table Project Data Analysis\Income.csv")

# defining Virginia Beach 2015 values
vb_income_group_data = data.query("county_name == 'Virginia Beach city' & year == 2015")['income_group_population']
vb_income_group_labels = data.query("county_name == 'Virginia Beach city' & year == 2015")['income_group']

# plot pie chart
plt.style.use('bmh')
plt.pie(vb_income_group_data, labels=vb_income_group_labels)
plt.show()