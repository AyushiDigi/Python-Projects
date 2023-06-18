#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/PT/Desktop/my python programs/genz.csv")
df.head(10)


# In[2]:


df.tail(10)


# In[3]:


df.shape


# In[4]:


df.columns


# In[5]:


df.info()


# In[7]:


df.describe()


# In[8]:


res= df.notnull()
print(res)


# In[9]:


country= df["Your Current Country."].value_counts()
print(country)


# In[93]:


g=['India','Germany','UAE',"USA"]
x= [231,2,1,1]
plt.figure(figsize=(4, 4))
sns.scatterplot(data=g, x=g, y=x, alpha=0.5, palette="husl",hue=g)
plt.xlabel("Countries",fontsize=9)
plt.ylabel('No. of people living in countries',fontsize=10)
plt.title('\n\nPolls for working in a company whose mission is not bringing social impact\n\n')
plt.xticks(rotation=90,fontsize=6) # Rotate x-axis tick labels by 90 degrees
plt.tight_layout()  # Ensure tight layout to prevent label overlapping
plt.legend(title='\n\nCountries\n\n',title_fontsize='8',prop={'size': 8},bbox_to_anchor=(1.02, 1), loc='upper left')
plt.show()


# In[13]:


f = df["Which of the below factors influence the most about your career aspirations ?"].value_counts()
print(f)


# In[26]:


colors = ['yellow', 'orange', 'red', 'skyblue', 'pink']
xy = [79, 57, 39, 37,23]
labels = ['My Parents', 'People who have changed the world for better', 'People from my circle, but not family members', 'Influencers who had successful careers',"Social Media like LinkedIn"]
plt.rcParams['font.size'] = 10

plt.figure(figsize=(4, 4))

plt.pie(xy, colors=colors, labels=labels, autopct='%1.1f%%', labeldistance=1.1, radius=1, startangle=180, textprops= {"fontsize": 8},wedgeprops={"edgecolor":"black"})  

plt.title("\nWhich of the below factors influence the most about your career aspirations ?\n\n\n")
plt.show()


# In[29]:


h= df["Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."].value_counts()
print(h)


# In[12]:


colors = ['#B7C3F3', '#DD7596', '#8EB897']
a = [110,65,60]
labels = ['Yes, I will earn and do that', 'No I would not be pursuing Higher Education outside of India', 'No, But if someone could bare the cost I will']
plt.rcParams['font.size'] = 10

plt.figure(figsize=(4, 4))

plt.pie(a, colors=colors, labels=labels,autopct='%1.1f%%', labeldistance=1.1, radius=1, startangle=180, textprops= {"fontsize": 8},wedgeprops={"edgecolor":"black"})  

plt.title("\nWould you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it.\n\n\n")
plt.show()


# In[5]:


i= df["How likely is that you will work for one employer for 3 years or more ?"].value_counts()
print(i)


# In[13]:


colors = ['lightcyan', 'lightcoral', 'khaki']
a = [110,65,60]
labels = ['This will be hard to do, but if it is the right company I would try', 'Will work for 3 years or more', 'No way, 3 years with one employer is crazy ']
plt.rcParams['font.size'] = 10

plt.figure(figsize=(4, 4))

plt.pie(a, colors=colors, labels=labels, autopct='%1.1f%%', labeldistance=1.1, radius=1, startangle=180, textprops= {"fontsize": 8},wedgeprops={"edgecolor":"black"})  

plt.title("\nHow likely is that you will work for one employer for 3 years or more ?\n\n\n")
plt.show()


# In[14]:


e= df["Would you work for a company whose mission is not clearly defined and publicly posted."].value_counts()
print(e)


# In[80]:


j = {"No":157, "Yes":78}
No = list(j.keys())
values = list(j.values())

fig = plt.figure(figsize=(5,5))

colors= ['indianred', 'greenyellow']
plt.bar(No,values,color=colors,width=0.3)
plt.margins(x=0.7)

plt.xlabel("\n\nResults of people who want to work for company whose mission is not defined\n\n")
plt.ylabel("\nVotes of people")
plt.title("\n\nWould you work for a company whose mission is not clearly defined and publicly posted.\n\n")
plt.show()


# In[25]:


g= df["How likely would you work for a company whose mission is misaligned with their public actions or even their product ?"].value_counts()
print(g)


# In[36]:


k = {"Will NOT work for them":158, "Will work for them":77}
keys = list(k.keys())
values = list(k.values())

fig = plt.figure(figsize=(5,5))

colors= ['peru', 'maroon']
plt.bar(keys,values,color=colors,width=0.3)
plt.margins(x=0.7)
plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels by 45 degrees
plt.subplots_adjust(bottom=0.2)  # Adjust the bottom margin to make space for the rotated labels


plt.xlabel("\n\npeople wants to work for company or not\n\n")
plt.ylabel("\nVotes of people")
plt.title("\n\nHow likely would you work for a company whose mission is misaligned with their public actions or even their product ?\n\n")
plt.show()


# In[38]:


l= df["How likely would you work for a company whose mission is not bringing social impact ?"].value_counts()
print(l)


# In[79]:


m = [5,8,7,6,1,3,4,2,10,9]
n= [49,34,31,26,25,19,18,16,10,7]
colors= ['black', 'turquoise']
plt.figure(figsize=(6, 6))
sns.scatterplot(data=m, x=m, y=n, alpha=0.5, palette="rocket",hue=m)
plt.title('\n\nPolls for working in a company whose mission is not bringing social impact\n\n')
plt.xlabel('Ratings',fontsize=8)
plt.ylabel('No. of Ratings',fontsize=10)
plt.xticks(rotation=90,fontsize=6) # Rotate x-axis tick labels by 90 degrees
plt.tight_layout()  # Ensure tight layout to prevent label overlapping
plt.legend(title='\n\nRatings\n\n',title_fontsize='8',prop={'size': 8},bbox_to_anchor=(1.02, 1), loc='upper left')
plt.show()


# In[8]:


env = df["What is the most preferred working environment for you."].value_counts()
print(env)


# In[42]:


v = ["Fully Remote with Options to travel as and when needed", "Hybrid Working Environment with less than 15 days a month at office","Every Day Office Environment","Hybrid Working Environment with less than 10 days a month at office","Hybrid Working Environment with less than 3 days a month at office ","Fully Remote with No option to visit offices"]
s= [60,57,50,31,26,11]

plt.figure(figsize=(6, 6))
sns.scatterplot(data=v, x=v, y=s, alpha=0.5, palette='dark',hue=v)
plt.title('\n\nWhat is the most preferred working environment for you.\n\n')
plt.xlabel('Preferred working environment',fontsize=8)
plt.ylabel('Votes',fontsize=10)
plt.xticks(rotation=90,fontsize=6) # Rotate x-axis tick labels by 90 degrees
plt.tight_layout()  # Ensure tight layout to prevent label overlapping
plt.legend(title='\n\nWorking environment\n\n',title_fontsize='8',prop={'size': 8},bbox_to_anchor=(1.02, 1), loc='upper left')
plt.show()

#prop size used for size decrease of hues


# In[43]:


emp = df["Which of the below Employers would you work with."].value_counts()
print(emp)


# In[53]:


colors = ['yellow', 'orange', 'red', 'skyblue', 'pink']
em = [113, 75, 36, 7,4]
ex=[0, 0, 0, 0,1]
labels = ['Employer who pushes your limits by enabling an learning environment, and rewards you at the end', 'Employer who appreciates learning and enables that environment', 'Employer who rewards learning and enables that environment', 'Employer who pushes your limits and doesnt enables learning environment and never rewards you',"\n\nEmployers who appreciates learning but doesn't enables an learning environment "]
plt.rcParams['font.size'] = 10

plt.figure(figsize=(3, 4))

plt.pie(em, colors=colors, labels=labels, autopct='%1.1f%%', labeldistance=1.1,explode=ex, radius=1, startangle=180, textprops= {"fontsize": 9},wedgeprops={"edgecolor":"black"})  

plt.title("\n\nWhich of the below Employers would you work with.\n\n")
plt.show()


# In[54]:


le = df["Which type of learning environment that you are most likely to work in ?"].value_counts()
print(le)


# In[65]:


colors = ['powderblue', 'peachpuff', 'violet', 'lawngreen', 'orange',"tan"]
em = [59, 45, 41,38,29,23]
ex=[0, 0, 0, 0,0,0]
labels = ["Self Paced Learning Portals, Instructor or Expert Learning Programs ","Instructor or Expert Learning Programs, Trial and error by doing side projects within the company", "Instructor or Expert Learning Programs, Learning by observing others", "Self Paced Learning Portals, Learning by observing others", "Learning by observing others, Trial and error by doing side projects within the company","Self Paced Learning Portals, Trial and error by doing side projects within the company"]
plt.rcParams['font.size'] = 10

plt.figure(figsize=(3, 4))

plt.pie(em, colors=colors, labels=labels, autopct='%1.1f%%', labeldistance=1.1,explode=ex, radius=1, startangle=180, textprops= {"fontsize": 9},wedgeprops={"edgecolor":"black"})  

plt.title("\n\nWhich type of learning environment that you are most likely to work in ?\n\n")
plt.show()


# In[68]:


ca = df["What type of Manager would you work without looking into your watch ?"].value_counts()
print(ca)


# In[74]:


colors = ['teal', 'lightsteelblue', 'thistle', 'grey',"peachpuff"]
lo = [129,45,37,21,3]
ex=[0, 0, 0, 0,1]
labels = ["Manager who explains what is expected, sets a goal and helps achieve it ", "Manager who clearly describes what she/he needs", "Manager who sets goal and helps me achieve it", "Manager who sets targets and expects me to achieve it ","Manager who sets unrealistic targets"]
plt.rcParams['font.size'] = 10

plt.figure(figsize=(3, 4))

plt.pie(lo, colors=colors, labels=labels, autopct='%1.1f%%', labeldistance=1.1,explode=ex, radius=1, startangle=180, textprops= {"fontsize": 9},wedgeprops={"edgecolor":"black"})  

plt.title("\n\nWhat type of Manager would you work without looking into your watch ?\n\n")
plt.show()

