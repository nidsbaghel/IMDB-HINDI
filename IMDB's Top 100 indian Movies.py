#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')
get_ipython().system('pip install html5lib')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[38]:


Page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
Page


# In[39]:


Page.content


# In[61]:


soup = BeautifulSoup(Page.content,'lxml')
soup


# In[69]:


import csv


# In[81]:



titles = [] 
for h3 in soup.find_all('h3'):
  titles.append(h3.string.strip())

ratings = []
for rating in soup.select('span.rating'):
  ratings.append(rating.string.strip())

lengths = []
for length in soup.select('span.length'):
  lengths.append(length.string.strip())

years = []
for year in soup.select('span.year'):
  years.append(year.string.strip())

 
with open('top100', 'w') as file:
    writer = csv.writer(file, delimiter=',')
  


# In[82]:


import pandas as pd 
pd.DataFrame({})
  writer.writerow(["title", "ratings",  "year"])
    for i in range(100):
    writer.writerow([
      titles[i], 
      ratings[i], 
      lengths[i], 
      years[i], 
      
    ])


# In[ ]:




