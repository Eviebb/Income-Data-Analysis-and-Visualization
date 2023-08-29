# import libraries
import pandas as pd
from matplotlib import pyplot as plt

# import data as data frame
data = pd.read_csv(r"C:\Users\Lorie\OneDrive\Desktop\Projects\US Income Table Project Data Analysis\Income.csv")

# income_group_population for rows in California
Cali_income_group_data = data.query("county_name == 'Virginia Beach city' & year == 2015")["income_group_population"]

# histogram of the California's recorded income groups
plt.style.use('bmh')
plt.hist(Cali_income_group_data, cumulative=True, color="#023020")
plt.show()