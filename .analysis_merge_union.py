
#%%

##### union файлов в один
import os
import glob
import pandas as pd
os.chdir("C:\\Users\\....Desktop\g\\")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep=";") for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


# %%
###################### Кейс: мердж данных с фильтрацией и первичным анализом полученных данных
import pandas as pd
#%%
import pandas as pd
data1 = pd.read_csv(r"C:\Users\........\full.csv" \
    , sep=',' , encoding='latin-1') #, index_col=0 - индекс 
data1.head()
# %%
data = pd.read_csv(r"C:\Users\vitaly.flerin\Desktop\05 Ad hoc\2022-08-12_ps_integrety\2022-10-27Детализация Калининград\ne.csv" \
    , sep=',' , encoding='latin-1')#, index_col=0 - индекс
data.head()     
# %% переименовавывем
data1= data1.rename(columns={"ï»¿recdate": "recdate"})
# %% дубликат столбца
data1['recdate_d'] = data1.loc[:, 'rec_dttm']
data1.head()
# %% перевод в дату
data1['recdate_d'] = pd.to_datetime(data1['recdate_d']).dt.date
data1.head()
# %% конверт к 1 числу
data1['recdate_d']=data1['recdate_d'].apply(lambda x: x.replace(day=1))
# %%перевод в дату
data['t1.report_date'] = pd.to_datetime(data['t1.report_date']).dt.date
data.head()
# %%мердж
qwe = pd.merge(data1, data, how='inner', left_on=['recdate_d', 'acell'] \
, right_on = ['t1.report_date','t1.acell'])
qwe.head()
# %%
data2 = qwe[['rec_dttm', 'acell', 'region', 'pi_share', \
     't1.report_date', 'sector_name',	't2.ne_id']]
data2.head()
# %%
# %%
data2.count
# %%
data2.to_csv('final_KK_1.csv', header=True, index=False)
# %%
data2.head()
# %%
data2.dtypes
# %%
data2["pi_share"] = data2.pi_share.astype(float)
# %%
data2["pi_share"] = [float(str(i).replace("100", "1")) for i in data2["pi_share"]]
#%%
len(data2)
# %%
data2.loc[(data2.pi_share =='0'), "pi_share"] = 0
# %%
data2.agg({'pi_share': ['count', 'sum']})
# %%
data2.pi_share.unique()
# %%
data2["pi_share"] = data2["pi_share"].str.replace('100', '1').astype(float)
# %%

