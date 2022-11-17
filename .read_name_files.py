# 
import os
nam=os.listdir(r"C:\Users\vitaly.flerin\Desktop\test_ vol")

# %%
import pandas as pd
nam = pd.DataFrame([nam])
# %%

# %%
import numpy as np
import pandas as pd
df = pd.DataFrame(np.array([nam]).T)
df.columns =['0']
df
# %%
df.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)

