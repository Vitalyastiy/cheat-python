#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as stats
# %%
df = sns.load_dataset("titanic")
df.head(5)
# %%
df.groupby("age", as_index = False).\
        agg({'age':"count"}).value_counts().hist(bins = 20)
# %%
df.age.hist()
# %%
sns.boxplot(df.age)
# %%
df.to_excel('qwe.xlsx')
# %%
df = pd.read_excel('qwe.xlsx')
# %%
df
# %%

rvs1 = df.age
rvs2 = df.fare
stats.ttest_ind(rvs1, rvs2)
# %%
rvs5 = stats.norm.rvs(loc=8, scale=20, size=100)
stats.ttest_ind(rvs1, rvs5)
# %%
df
# %%
