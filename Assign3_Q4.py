# -*- coding: utf-8 -*-
"""

@author: user
"""

import pandas as pd
import numpy as np
from scipy import stats as stats
from scipy.stats import chi2_contingency
from scipy.stats import chi2

df = pd.read_csv('Costomer+OrderForm.csv')
df.head()
    
print(df['Phillippines'].value_counts(),df['Indonesia'].value_counts(), df['Malta'].value_counts(),df['India'].value_counts())

observed=([[271,267,269,280],[29,33,31,20]])    #observed values

#Applying Chi-Square contingency table to convert observed value into expected value
stat, p, dof, expected = chi2_contingency([[271,267,269,280],[29,33,31,20]])
stat
p                        #pvalue
dof                     #Degrees of freedom
expected               #expected values

observed = np.array([271, 267, 269, 280, 29, 33, 31, 20])
expected = np.array([271.75, 271.75, 271.75, 271.75, 28.25, 28.25, 28.25, 28.25])

#Compare Evidences with Hypothesis using t-statictic
test_statistic , p_value = stats.chisquare(observed, expected,dof)
print("Test Statistic = ",test_statistic,'\n', 'p_value =',p_value)

alpha = 0.05

print('significance=%.3f, p=%.3f' % (alpha, p_value))
if p_value <= alpha:
	print("Ho is rejected & H1 is accepted")
else:
	print("H0 is accepted & H1 is rejected")