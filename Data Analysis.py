data_head = data.head
data_shape = data.shape
data_index = data.index
data_columns = data.columns
data_types = data.dtypes
unique_values = data['income_group'].unique() #only on individual columns
nunique_values = data.nunique()#single column and individual columns
data_value_counts = data['income_group'].value_counts()#shows unique values and their count
data_info = data.info()

#plt.subplot_tool()
