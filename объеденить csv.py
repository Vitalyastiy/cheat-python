# %%

import os
import glob
import pandas as pd
os.chdir("C:\\Users\\vitaly.flerin\\Desktop\\new\\")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep=";") for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
#%%
from itertools import count
from multiprocessing import cpu_count
import pandas as pd
data = pd.read_csv(r"C:\Users\vitaly.flerin\Desktop\new\duble.csv" \
    , sep=';' , encoding='ISO-8859-1',  on_bad_lines='skip') #, index_col=0 - индекс 
data


# %%
import os
import glob
import pandas as pd
data1 = pd.read_csv(r"C:\Users\vitaly.flerin\Desktop\05 Ad hoc\2022-08-12_ps_integrety\2022-10-27Детализация Калининград\combined_csv.csv" \
    , sep=',' , encoding='latin-1') #, index_col=0 - индекс 
data1.head(3)
# %%
data=data.rename(columns={"ï»¿RECDATE": "rec_dttm", \
    "Mean_flag_integrity 4G (%)": "pi_share", "ACELL":"acell", \
        "Region":"region"  } )
data.head(3)
# %%
data1=data[["rec_dttm", "acell", "region",  "pi_share"]]
data1.head(3)

# %%
data1.to_csv('full.csv', header=True, index=False)
# %%
data.head()
# %%
data = pd.read_csv(r"C:\Users\vitaly.flerin\Desktop\05 Ad hoc\2022-08-12_ps_integrety\2022-10-27Детализация Калининград\ne.csv" \
    , sep=',' , encoding='latin-1') #, index_col=0 - индекс 
data.head(3)
# %%
data.head(3)
# %%
data1.head(3)
# %%
data1['rec_dttm'] = pd.to_datetime(data1['rec_dttm']).dt.date
data1
# %%
data1["Mean_flag_integrity 4G (%)"].unique()
# %%
