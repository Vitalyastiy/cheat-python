#%%

############################## Тест Фишера ####################

#аналог хи-2, если мало значений
data = [[8, 4],
 [4, 9]]
import scipy.stats as stats
print(stats.fisher_exact(data))
(4.5, 0.1152)

#%%
############################## Тест Левина на равенство дисперсий ####################

from scipy.stats import levene
# define groups
group_1 = [ 14 , 34 , 16 , 43 , 45 , 36 , 42 , 43 , 16 , 27 ]
group_2 = [ 34 , 36 , 44 , 18 , 42 , 39 , 16 , 35 , 15 , 33 ]
# define alpha
alpha = 0.05
# now we pass the groups and center value from the following
# ('trimmed mean', 'mean', 'median')
w_stats, p_value = levene(group_1,group_2, center = 'mean' )
if p_value > alpha :
    print ( "We do not reject the null hypothesis" )
else:
    print( "Reject the Null Hypothesis" )
#-------------------------------------------------------------    
# %%

### Доверительный интервал ######
from numpy import sqrt
from scipy import stats
p = 0.99
mean = 10
std = 5
n = 100
se = std/sqrt(n)
alpha = (1-p)/2
sigma = stats.norm().isf(alpha)
сonfidence_interval = mean - sigma*se, mean + sigma*se
print('[%.2f; %.2f]' % сonfidence_interval)

#%%
#--------------------------------------------------------------------------------
######## Ящик с усами, проверка гипотезы ###########
from scipy import stats
import pandas as pd

# Выборки которые надо сравнить
data = pd.DataFrame({
           'a': [3, 1, 2],
           'b': [5, 3, 4],
           'c': [7, 6, 5]
          })
data.boxplot()
print('Нулевая гипотеза:', '='.join(data))
print('Альтернативная гипотеза:', f'!({"=".join(data)})')
# общая средняя
grand_mean = data.values.flatten().mean()
# отклонение групповых средний от общей средней
ssb = sum(data[group].size * (group_mean - grand_mean)**2  for group, group_mean in data.mean().items())
# отклонения значений в внутри группы от средней группы
ssw = sum(sum((x - group_mean)**2 for x in data[group]) for group, group_mean in data.mean().items())

groups = data.shape[1]
dfb = groups - 1
dfw = data.size - groups
# межгрупповой средний квадрат  
mssb = ssb/dfb
# внутригрупповой средний квадрат
mssw = ssw/dfw
f_value = mssb/mssw
p = stats.f.sf(f_value, dfb, dfw)
print('Результат:')
if p < 0.05:
    print('отклоняем нулевую гипотезу')
else:
    print('НЕ отклоняем нулевую гипотезу')

# %%
#интервал
def conf_interval_norm(М_mean, sd, n, accuracy):
    se = sd/(n**(1/2))
    if accuracy == 95:
        di_1 = М_mean - se*1.96
        di_2 = М_mean + se*1.96
        print(f'Доверительный интервал для среднего: [{di_1} ; {di_2}]')
    elif accuracy == 99:
        di_1 = М_mean - se*2.58
        di_2 = М_mean + se*2.58
        print(f'Доверительный интервал для среднего: [{di_1} ; {di_2}]')
              
conf_interval_norm(7, 4, 100, 95)
# %%
