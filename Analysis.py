#!/usr/bin/env python
# coding: utf-8

# ## Importing Libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
import sqlite3
import folium

get_ipython().run_line_magic('pip', 'install geopy')
from geopy.geocoders import Nominatim

from matplotlib.colors import LinearSegmentedColormap
from IPython.display import display
import warnings
warnings.filterwarnings('ignore')


# ## Database Connection

# In[2]:


#creating database connection
conn = sqlite3.connect('yelp.db')


# In[3]:


tables = pd.read_sql_query("SELECT name from sqlite_master where type = 'table'", conn)


# In[4]:


tables


# In[6]:


# explore the type of data available in the tables
for table in tables['name']:
    display(pd.read_sql_query(f"select * from {table} limit 5", conn))


# ## Data Analysis

# In[7]:


pd.read_sql_query("select count(*) from business", conn)


# In[20]:


business_id = pd.read_sql_query("""select business_id, review_count from business where lower(categories) like '%restaurant%' and is_open =1""", conn)


# In[21]:


# What is the descriptive stats for review count and star rating for businesses?
# avg, min, max, median
pd.read_sql_query(f"""
SELECT avg(review_count), 
min(review_count), 
max(review_count) AS max_review_count ,
(SELECT review_count from business order by review_count limit 1 offset (select count(*) from business) /2) as median_review_count,

avg(stars) AS average_star_rating,
MIN(stars) AS min_star_rating,
MAX(stars) AS max_star_rating,
(SELECT stars FROM business ORDER BY stars LIMIT 1 OFFSET(SELECT COUNT(*) FROM business) /2) AS median_star_rating

from business
where business_id IN {tuple(business_id['business_id'])};

""", conn).transpose()


# In[24]:


def remove_outliers(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df


# In[25]:


business_id = remove_outliers(business_id, 'review_count')


# In[26]:


business_id.shape


# In[27]:


pd.read_sql_query(f"""
SELECT avg(review_count), 
min(review_count), 
max(review_count) AS max_review_count ,
(SELECT review_count from business order by review_count limit 1 offset (select count(*) from business) /2) as median_review_count,

avg(stars) AS average_star_rating,
MIN(stars) AS min_star_rating,
MAX(stars) AS max_star_rating,
(SELECT stars FROM business ORDER BY stars LIMIT 1 OFFSET(SELECT COUNT(*) FROM business) /2) AS median_star_rating

from business
where business_id IN {tuple(business_id['business_id'])};

""", conn).transpose()


# In[ ]:


# Which restaurants have the highest number of reviews?


