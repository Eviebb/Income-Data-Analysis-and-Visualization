data_head = data.head
data_shape = data.shape
data_index = data.index
data_columns = data.columns
data_types = data.dtypes
unique_values = data['income_group'].unique() #only on individual columns
nunique_values = data.nunique()#single column and individual columns
data_value_counts = data['income_group'].value_counts()#shows unique values and their count
data_info = data.info()

#scrapped


# bar plot
income_barplot = sns.barplot(x = 'income_group_population', y = 'state_name')
print(plt.show())
#income_scatterplot = sns.scatterplot(x='income_group_population', y='total_population_all_income_groups', data=data)