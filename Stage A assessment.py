#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd 
data = pd.read_excel("C:\\Users\\mayok\\Downloads\\FoodBalanceSheets_E_Africa_NOFLAG (1).xlsx", encoding='latin-1')
#test data("C:\\Users\\mayok\\Downloads\\FoodBalanceSheets_E_Africa_NOFLAG (1).xlsx", encoding='latin-1')
print (data)
data_duplicates = data.duplicated().any()
data_area =data.groupby('Area')['Area'].count()
print(data_area)

#correlation
data_Y2014 = Y2014.iloc


# In[20]:


2 + 2


# In[ ]:





# In[ ]:




