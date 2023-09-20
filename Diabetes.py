#!/usr/bin/env python
# coding: utf-8

# ![63329Diabetes%20Prediction%201.jpg](attachment:63329Diabetes%20Prediction%201.jpg)

# # Importing Required Libraries

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy 
from matplotlib.colors import ListedColormap
import warnings
warnings.filterwarnings('ignore')


# # Importing Required Data Set

# In[2]:


df=pd.read_csv("diabetes.csv",encoding='ISO-8859-1')
print(df)


# # Understanding the Data Set

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[7]:


df.info()


# In[8]:


df.columns


# # Finding Null Values

# In[9]:


df.isnull()


# In[10]:


df.isnull().sum()


# # There are no null values so we can start the analysis

# # Performing EDA- EXPLORATORY DATA ANALYSIS

# In[11]:


plt.figure(figsize=(12, 6))
for i, col in enumerate(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']):
    plt.subplot(2, 4, i + 1)
    df[col].hist(bins=20, edgecolor='k')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# In[12]:


# 1.2: Countplot for the 'Outcome' variable (target variable)
plt.figure(figsize=(6, 4))
sns.countplot(x='Outcome', data=df)
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.title('Distribution of Outcomes')
plt.show()


# In[16]:


# 3.1: Correlation heatmap to visualize relationships between numerical variables
correlation_matrix = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


# In[18]:


plt.figure(figsize=(12, 6))
for i, col in enumerate(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']):
    plt.subplot(2, 4, i + 1)
    sns.boxenplot(x='Outcome', y=col, data=df)
    plt.xlabel('Outcome')
    plt.ylabel(col)
plt.tight_layout()
plt.show()


# In[22]:


plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(df['Age'], df['BloodPressure'], alpha=0.5)
plt.xlabel('Age')
plt.ylabel('BloodPressure')
plt.title('Scatter Plot of BloodPressure vs. Age')

# Scatter plot of DiabetesPedigreeFunction vs. Age
plt.subplot(1, 2, 2)
plt.scatter(df['Age'], df['DiabetesPedigreeFunction'], alpha=0.5)
plt.xlabel('Age')
plt.ylabel('DiabetesPedigreeFunction')
plt.title('Scatter Plot of DiabetesPedigreeFunction vs. Age')

plt.tight_layout()
plt.show()


# In[23]:


plt.figure(figsize=(12, 8))
for i, col in enumerate(['Glucose', 'Insulin', 'BMI', 'Age']):
    plt.subplot(2, 2, i + 1)
    plt.hist(df[col], bins=20, edgecolor='k')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()


# In[26]:


from pandas.plotting import scatter_matrix
scatter_matrix(df[['Glucose', 'Insulin', 'BMI', 'Age']], figsize=(12, 12), alpha=0.5)
plt.show()


# In[27]:


correlation_matrix = df[['Glucose', 'Insulin', 'BMI', 'Age']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


# In[33]:


plt.figure(figsize=(10, 6))
sns.barplot(x='Pregnancies', y='BloodPressure', data=df, ci=None)
plt.xlabel('Pregnancies')
plt.ylabel('Average BloodPressure')
plt.title('Average BloodPressure by Number of Pregnancies')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




