# %%
#### импорт библиотек и загрузка данных во фрейм ####
from itertools import count
from multiprocessing import cpu_count
import pandas as pd
data2 = pd.read_csv(r"C:\Users\....Desktop\nnn\NN.csv" \
    , sep=',' , encoding='latin-1') #, index_col=0 - индекс 
data2.head(3)
#%%
'''data = pd.read_csv(r"C:\Users\...Desktop\nn\02-03_new — копия.csv" \
    , sep=',' , encoding='latin-1') #, index_col=0 - индекс 
data.head(3)'''
# data_copy[:10].to_csv('saved_ratings.csv', index=False) # экспортироватъ первые десятъ строк
# data_copy = data.copy(deep=True) #shallow - поверхностное копирование фрейма 

#data1.to_csv('02-03_new.csv', header=True, index=False) # экспорт в csv
# %%

######### Переименовать данные 
data=data.rename(columns={"Mean_flag_integrity 4G (%)": "flag"}) # переименовать
data= data.rename(columns={"gkgk": "colu"}) # - переименоватъ столбец
data.rename(columns=dict(sector_name='region', region='locale')) # - переименоватъ столбец
data.rename(index={0: 'firstEntry', 1: 'secondEntry'}) # переименовать индекс
data.rename_axis('inde', axis='rows') # переименовать название 

#########   Работа с выбором значений 
data.sample(5) # data.head(5) # data.tail(5)  # выбор выборки
data.head(3) # - вывести первые 3 записи
data_copy.tail(1) # - вывести последнюю записъ
data[1:4] # - вывести топ значений фрейма 

######## |Первичный Анализ 
data.columns.tolist() # - получитъ наименования столбцов списком
data.acell.value_counts() # - подсчет количества уникалных значений
len(data) # - вывести количество строк во фрейме 
len(data['t2.ne_id'].unique()) # - количество уникалъных строк во фрейме 
data.info() # - получение сведений о фрейме 
data.describe # - статистическая информация о фрейме
data ['acell'].tolist() # - перевести в список стлбец 
data['colu'] = True # - добавитъ столбец во фрейм данных
data2= data[['acell', 'colu']] # - создание нового фрейма из подмножества
data2.drop(['colu'], axis=1).head() # - удаление столбца из фрейма данных
data2.append(data2.sum(axis=0), ignore_index=True) # - сумма по столбцу
data[data['acell'].isin(['NN002998_I','NN002998_I'])] # -филътр
data[data['acell'] == 'NN002998_I'] #(><) -филътр, для единственного значения
data.sort_values('acell', ascending=True) # - сортировка фрейма 
data['t2.ne_id'].astype('float') # - изменить тип данных
data['sector_name'].fillna('NaN').value_counts().sort_values(ascending=False) # найти NaN

## группировка с выводом стат. данных
data.groupby('t1.acell').count()
data.groupby('t1.acell').mean()
data.groupby('t1.acell').median()

## подчсчитать количество нулевых значений
m_data = data[data['sector_name'].isnull()]
n_data = len(m_data) # v1

n_data = data.sector_name.isnull().sum() # v2
m_data = pd.isnull(data.sector_name).sum() # v3

## объеденение данных:
pd.concat([df1, df2], ignore_index=True)  # - union
sum_df = pd.merge(df1, df2, how='inner', left_on=['t1.region', 't1.acell'] \
, right_on = ['Region','ACELL']) # merge
data1 = pd.concat([data, data2]) # union

###кейс с фильтрацией:
data['t1.region'].unique() #  вывести уникальные значения фрейма
data = data.set_index('t1.region') # присвоить индекс
data.drop(['RYAZAN', 'TVER'],axis = 0) # установить фильтрацию по столбцу и дропнуть эти данные во фрейме 

##### Детальный анализ и группировка
data.groupby('t1.acell').count() # - группировка для фрейма

# группирвка таблицы:
data.groupby(["t1.acell"]).agg({
  "t2.ne_id": "sum",
  "t1.region": "count",
  "t1.macroregion": "last"
}).reset_index()

# Перебор строк во фрейме()
for idx,row in df2[:1].iterrows():
    print(idx, row)
#%%
############### loc/iloc     ##############
data.iloc[:0]  # вывести шапку 
data.iloc[552] # вывод СПИСОК строки по номеру
data.iloc[552] # вывод строки по индексу
data.iloc[0:5] # вывести первые 5 значений, с 0 до 4  
data.loc[0:5]  # вывести первые 6 значений, с 0 до 5

data.recdate  #data['recdate'] #data.iloc[:,0]#  вывод столбца в формате списка
data.iloc[2,1] # data.loc[2,'ACELL'] вывести 3 строку из 2-ого столбца 
data.iloc[:3,1] #data.iloc[0:3,1]#data.iloc[[0,1,2],1]  вывести количество строк из столбца
data.iloc[-3:,1] #  вывести второе значение снизу, второго столбца
data.iloc[:, 0:2] # вывести всю информацию по двум столбцам  
data.iloc[3, [1, 2, 3]] # список третьей строки по первым 3м столбцам
data.loc[1:5, 'ACELL': 'Region'] # вывод таблицы с первой по пятаю, 2 столбца 

data.iloc[[0]] # вывести первую строку
data.loc[:,['recdate','ACELL','Region','flag']] # print all
data.loc[data.flag.isin(['100', '50'])] # филътр несколъко условий
data.loc[data.flag.isnull()] 
data.loc[data.flag.notnull()]  
data[data['t2.ne_id'].isnull()] # вариация поиска нулевых значений

############## Примеры фильтров выводом фрейма 
data.loc[data['ACELL'] == 'NN000231_A'] # вывести отфильтрованную таблицу
data.loc[data.ACELL == 'NN000231_A'] # то же что и предыдущее
data.loc[data.flag == '0'] # филътр на таблицу с выводом всего датафрейма 

data.loc[(data.flag == '0') & (data.recdate =='2022-02-28 23:00')] # склеенный фильтр на таблицу
data.loc[(data['ACELL'] == 'NN000231_A' ) & (data['recdate'] == '2022-02-20 16:00')\
    , 'recdate':'flag'] # пример склеенного фильтра

###### replace ###### 
data.loc[data['ACELL'] == 'NN000231_A'] = 'BIG'
data.loc[data['ACELL'] == 'NN000231_A', 'ACELL':'Mean_flag_integrity 4G (%)'].head() # пример реплэйса с фильтром и выводом

############# группировка данных
data.groupby('report_date').report_date.size() #(count-разница?) вывести количество записей, аналог гроуп бай
data.groupby('t1.acell')['t2.ne_id'].max().sort_index() # присваиваем индекс аселу и выводим макимальное значение из не_ид, сортируем от меньшего 
data_e = data.groupby(['t1.acell']).ne_id.agg([len, min, max]) # группировка с агрегацией и расчетом 
data_e.sort_values(by=['min', 'max'], ascending=True) # сортировка данных 
data.groupby('t1.acell').ne_id.mean() # найти среднее значение  
data.groupby(['t1.acell', 'ne_id']).size().sort_values(ascending=False) # группировка по значению
#%%
#
####
###########
###################   Other...
df = data.append(new_row, ignore_index=True) # добавляет элемент в конец списка
df = data.drop(['t1.macroregion'], axis = 1) # удалить столбец
df_copied = df.copy() # поверхностное и глубокое копирование 
df['vol_new'] = round(df['ut_driver']) # округлить до выделенного значения 
#%%
