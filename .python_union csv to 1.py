# %%

import os
import glob
import pandas as pd
os.chdir("C:\\Users\\....\\Desktop\\new\\")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep=";") for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
#%%



''' Для экселя'''
# filenames
excel_names = ["yan_1.xlsx", "yan_2.xlsx", "yan_3.xlsx", "yan_4.xlsx"]
# read them in
excels = [pd.ExcelFile(name) for name in excel_names]
# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]
# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]
# concatenate them..
combined = pd.concat(frames)
# write it out
combined.to_excel("pivot.xlsx", header=False, index=False)
