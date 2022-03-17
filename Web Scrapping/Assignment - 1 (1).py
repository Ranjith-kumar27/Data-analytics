#!/usr/bin/env python
# coding: utf-8

# In[69]:


pip install bs4


# In[70]:


pip install requests


# In[71]:


import requests

from bs4 import BeautifulSoup


# In[72]:


url = 'https://www.zigwheels.com/newbikes/best-bikes-in-india'


# In[73]:


response = requests.get(url)


# In[74]:


response


# In[75]:


Bikes = BeautifulSoup(response.text)


# In[76]:


Bikes


# In[77]:


Name = Bikes.select('.ht-name')


# In[78]:


Name


# In[81]:


Name_list = []
Name_link = []


# In[82]:


for item in Name:
    Name_list.append(item.text)
    link = "https://www.zigwheels.com"+ item ["href"]
    Name_link.append(link)


# In[83]:


Name_list


# In[84]:


Price = Bikes.select('#modelList .fnt-black')


# In[85]:


Price


# In[86]:


Price_rs = []


# In[87]:


for item in Price:
    Price_rs.append(item.text)


# In[88]:


Price_rs


# In[89]:


rating = Bikes.select('.rt-lg')


# In[90]:


rating


# In[91]:


rating_list = []


# In[92]:


for item in rating:
    rating_list.append(item.text)


# In[93]:


rating_list


# In[94]:


spec = Bikes.select('.ht-spec')


# In[95]:


spec


# In[96]:


spec_list = []


# In[97]:


for item in spec:
    spec_list.append(item.text)


# In[98]:


spec_list


# In[99]:


review = Bikes.select('.i-b.lnk-c')


# In[100]:


review


# In[101]:


review_list = []


# In[102]:


for item in review:
    review_list.append(item.text)


# In[103]:


review_list


# In[104]:


import pandas as pd


# In[105]:


Name = pd.DataFrame(Name_list,columns=['Name'])


# In[106]:


Name


# In[107]:


Price = pd.DataFrame(Price_rs,columns=['Price'])


# In[108]:


Price


# In[109]:


rating = pd.DataFrame(rating_list,columns=['rating'])


# In[110]:


rating


# In[111]:


spec = pd.DataFrame(spec_list,columns=['spec'])


# In[112]:


spec


# In[113]:


review = pd.DataFrame(review_list,columns=['review'])


# In[114]:


review


# In[115]:


Name['Price'] = Price


# In[116]:


Name['rating'] = rating


# In[117]:


Name['spec'] = spec


# In[118]:


Name['review'] = review


# In[119]:


Name


# In[121]:


Name.to_csv('Name.csv')

