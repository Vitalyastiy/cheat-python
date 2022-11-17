
# %%
import openpyxl
import pandas as pd
# Load the xlsx file
excel_data = pd.read_excel(r"C:\Users\vitaly.flerin\Desktop\w\NN.xlsx")
# Read the values of the file in the dataframe
excel_data.rename(columns={'a.start_time':'start_time' , 'a.ne_id':'ne_id',	\
    'a.subs_id':'subs_id',	'start_time_r':'start_time_r' }, inplace = True)

excel_data

# %%

data = excel_data
data=data.loc[data['start_time_r'] == '2022-08-31 20:00:00.0'] 

# %%
data['subs_id', 'start_time_r']
# %%
df = data.drop('start_time', axis=1)
# %%
df
# %%
