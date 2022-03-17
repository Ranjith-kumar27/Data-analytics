#!/usr/bin/env python
# coding: utf-8

# In[58]:


pip install bs4


# In[59]:


pip install requests


# In[60]:


import requests

from bs4 import BeautifulSoup


# In[61]:


url = 'https://ecommerceguide.com/top/top-10-ecommerce-sites-in-india/'


# In[62]:


response = requests.get(url)


# In[63]:


response


# In[64]:


Ecom = BeautifulSoup(response.text)


# In[65]:


Ecom


# In[66]:


site = Ecom.select('strong a')


# In[67]:


site


# In[68]:


site_list = []


# In[69]:


for item in site:
    site_list.append(item.text)


# In[70]:


site_list


# In[79]:


img = Ecom.select('.lazyloaded')


# In[80]:


img


# In[81]:


img_r = []


# In[82]:


for item in img:
    img_r.append(item.text)


# In[83]:


img_r


# In[84]:


import pandas as pd


# In[85]:


site = pd.DataFrame(site_list,columns=['Name'])


# In[86]:


site


# In[87]:


site['img'] = img_r


# In[52]:


site.to_csv('imdb.csv')

