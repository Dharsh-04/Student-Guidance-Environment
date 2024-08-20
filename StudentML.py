#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pickle

# In[3]:


df=pd.read_csv(r"C:\Users\Admin\Desktop\sample1.csv")


# In[4]:


df.head()


# In[5]:


df.isnull().sum()


# In[6]:


df.fillna(method='ffill',inplace=True)
df


# In[7]:


df.isnull().sum()


# In[8]:


df.columns


# In[9]:


x=df[['Course','GPA','Workshops Attended','Projects Done','Club Participation',' Skills Acquired']]
x


# In[10]:


y=df[['RESULT']]
y


# In[11]:


x=df.iloc[:,:-1]
x


# In[12]:


y=df.iloc[:,-1]
y


# In[13]:


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)


# In[14]:


from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

clf = RandomForestClassifier()
clf.fit(x, y)
ypred=clf.predict(xtest)
accuracy = accuracy_score(ypred, ytest)
print("Accuracy:", accuracy)


# In[15]:


pre= clf.predict([['1','1','1','1','1','1']])
pre
pickle.dump(clf,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
model

# In[ ]:




