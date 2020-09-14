#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'datasets/gradedata.db'
engine = create_engine(r"sqlite:///{}"
        .format(db_file))
sql = 'SELECT * from test'
        'where Grades in (76,77,78)'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df


# In[2]:


sql = "select name from sqlite_master"
    "where type = 'table';"


# In[3]:


sql = "select * from test;"


# In[4]:


sales_data_df.head()


# In[ ]:




