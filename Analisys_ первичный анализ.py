
# %%
data=data.rename(columns={"Mean_flag_integrity 4G (%)": "flag"})
data.head(3)

import pandas as pd
data1 = pd.read_csv(r"C:\Users\vitaly.flerin\Desktop\05 Ad hoc\2022-08-12_ps_integrety\2022-10-27Детализация Калининград\full.csv" \
    , sep=',' , encoding='latin-1') #, index_col=0 - индекс 
data1.head()               
# %%

data.flag == '0' # Филътр, вывод списком 
data[['ACELL', 'Region']] # фильтр на 2 стобца
data.ACELL == 'NN000231_A' # выводит булево, оценивая каждую строку по отдельности 
data['flag']=range(len(data),0,-1) # -заменить индексом столбец, в обратном порядке
data_i=data.set_index('ACELL')# присвоитъ индекс ???
# %%
# %%
data.loc[(data.nps==1) | (data.Negative_hours>1)]
# %%
data.columns = data.columns.str.replace(' ', '_')
# %%
q=data.loc[(data.Negative_hours.notnull()) & (data.nps==1)]
# %%
data.groupby('nps', as_index=False).agg({'acell':'count'}) \
    .sort_values('acell', ascending=True)
# %%
data[data.Negative_events>0].groupby('nps', as_index=False) \
    .agg({'acell':pd.Series.nunique}) \
        .sort_values('acell', ascending=True)#подсчет уникалных
# %%
dar = data.query("acell == 7 & nps == 1" )
# %%
dar.groupby('sector_name',as_index=False) \
    .agg({'No_Negative_hours':'sum'}) \
        .rename(columns={'No_Negative_hours' : 'SU_NNH'}) \
            .sort_values('SU_NNH', ascending=True).SU_NNH.mean        
# %%
data.describe
# %%
data.nps.acell.nunique().plot()