
# coding: utf-8

# In[2]:


import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

#to display all rows columns 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)


# In[2]:


# ipl_ball_by_ball_data


# In[3]:


df = pd.read_csv('ipl_ball_by_ball_updated.csv')


# In[4]:


df.head(1)


# In[5]:


df.innings.unique()


# In[6]:


df = df[(df.innings == 1) | (df.innings == 2)]


# In[7]:


df.innings.unique()


# In[8]:


# What are the numbers when Maxwell faces Ashwin?
# step 1: Filter by player names - Done
# step 2: Use these names & assign it to striker & bowler - Done
# step 3: Get the required columns - Done


# In[8]:


df.bowling_team.unique()


# In[32]:


df[df.bowling_team == 'Chennai Super Kings']['bowler'].unique()


# In[11]:


# player 1: R Ashwin
# player 2: Maxwell


# In[31]:


df[df.batting_team == 'Kings XI Punjab']['striker'].unique()


# In[33]:


req_df = df[(df.striker == 'GJ Maxwell') & (df.bowler == 'R Ashwin')]


# In[34]:


req_df.head()


# In[15]:


# No of runs scored?
# No of balls faced?
# No of times dismissed?


# In[123]:


# runs scored
sum(req_df.runs_off_bat)


# In[124]:


# balls faced
len(req_df)


# In[125]:


# outs
len(req_df[req_df.player_dismissed == 'GJ Maxwell'])


# In[99]:


res_df = df[(df.striker == 'CH Gayle') & (df.bowler == 'R Ashwin')]


# In[100]:


res_df


# In[106]:


sum(res_df.runs_off_bat),len(res_df),len(res_df[res_df.player_dismissed == 'CH Gayle'])


# In[108]:


# balls faced
rew_df = df[(df.striker == 'PA Patel') & (df.bowler == 'R Ashwin')]


# In[109]:


sum(rew_df.runs_off_bat),len(rew_df),len(rew_df[rew_df.player_dismissed == 'PA Patel'])


# In[119]:


gamb_df = df[(df.striker == 'G Gambhir') & (df.bowler == 'R Ashwin')]


# In[120]:


sum(gamb_df.runs_off_bat),len(gamb_df),len(gamb_df[gamb_df.player_dismissed == 'G Gambhir'])


# In[116]:


kock_df = df[(df.striker == 'Q de Kock') & (df.bowler == 'R Ashwin')]


# In[117]:


sum(kock_df.runs_off_bat),len(kock_df),len(kock_df[kock_df.player_dismissed == 'Q de Kock'])


# In[121]:


rana_df = df[(df.striker == 'N Rana') & (df.bowler == 'R Ashwin')]


# In[122]:


sum(rana_df.runs_off_bat),len(rana_df),len(rana_df[rana_df.player_dismissed == 'N Rana'])


# In[ ]:


N Rana


# In[39]:


# strike rate
100*sum(req_df.runs_off_bat)/len(req_df)


# In[22]:


# Comparision against all batsman Ashwin has bowled to


# In[40]:


df.head(1)


# In[48]:


ashwin_df = df[df.bowler =='R Ashwin']


# In[49]:


ashwin_df.head()


# In[52]:


# runs scored by this batsman
bdf1 = pd.DataFrame(ashwin_df.groupby('striker')['runs_off_bat'].sum()).reset_index()


# In[53]:


bdf2 = pd.DataFrame(ashwin_df.groupby('striker')['ball'].count()).reset_index()


# In[54]:


bdf2.head()


# In[55]:


bdf3 = bdf1.merge(bdf2, on = 'striker', how = 'left')


# In[56]:


bdf3.head(1)


# In[57]:


bdf3['strike_rate'] = 100*bdf3['runs_off_bat']/bdf3['ball']


# In[58]:


bdf3.head(1)


# In[41]:


# min criteria: 30 balls


# In[59]:


bdf3 = bdf3[bdf3.ball >= 30]


# In[126]:


bdf3.head(20)


# In[61]:


abd_df = df[df.striker =='GJ Maxwell']


# In[62]:


# runs scored by this batsman
adf1 = pd.DataFrame(abd_df.groupby('bowler')['runs_off_bat'].sum()).reset_index()


# In[63]:


adf1.head()


# In[64]:


# balls faced
adf2 = pd.DataFrame(abd_df.groupby('bowler')['ball'].count()).reset_index()


# In[65]:


adf2.head()


# In[66]:


adf3 = adf1.merge(adf2, on = 'bowler', how = 'left')


# In[67]:


adf3.head(1)


# In[88]:


adf3['strike_rate'] = 100*adf3['runs_off_bat']/adf3['ball']


# In[130]:


adf3.head()


# In[53]:


# min criteria : 30 balls


# In[131]:


adf3 = adf3[adf3.ball >= 30]


# In[132]:


adf3.head()


# In[134]:


data=adf3.sort_values('strike_rate', ascending = False)
data


# In[135]:


data.to_csv('maxwell vs all.csv',index=None)


# In[55]:


# bdf3, adf3


# In[71]:


bdf3.reset_index(inplace = True, drop = True)
adf3.reset_index(inplace = True, drop = True)


# In[72]:


bdf3.head()


# In[90]:


bdf3.sort_values('strike_rate', ascending = False)


# In[79]:


adf3.sort_values('strike_rate', ascending = False)


# In[73]:


plt.figure(figsize = (16, 8))
plt.scatter(bdf3.strike_rate, bdf3.runs_off_bat)

for i in range(len(bdf3)):
#     plt.text(x, y, text)
    if bdf3['striker'][i] == 'GJ Maxwell':
        plt.text(bdf3['strike_rate'][i] - 7, bdf3['runs_off_bat'][i] - 1, bdf3['striker'][i] )
    else:
        plt.text(bdf3['strike_rate'][i] + 1, bdf3['runs_off_bat'][i] - 1, bdf3['striker'][i] )

plt.axvline(120, ls = '--', color = 'grey')
plt.axhline(60, ls = '--', color = 'grey')
plt.title('Batsman against R ashwin in IPL (min 30 balls faced)', fontsize = 20)
plt.xlabel('Strike rate')
plt.ylabel('Runs scored')
plt.show()


# In[128]:


plt.figure(figsize = (16,8))
plt.rcParams['axes.facecolor'] = '#fff7fb'
plt.scatter(bdf3.strike_rate, bdf3.runs_off_bat)

for i in range(len(bdf3)):
    if bdf3.striker[i] == 'V Kohli':
        plt.text(bdf3.strike_rate[i] - 7, bdf3.runs_off_bat[i] - 1, bdf3.striker[i])
    elif bdf3.striker[i] == 'GJ Maxwell':
        plt.text(bdf3.strike_rate[i] + 2, bdf3.runs_off_bat[i] - 1, bdf3.striker[i], color = 'maroon')
    elif (bdf3.striker[i] == 'N Rana') | (bdf3.striker[i] == 'KL Rahul') | (bdf3.striker[i] == 'JP Duminy'):
        plt.text(bdf3.strike_rate[i] + 2, bdf3.runs_off_bat[i] - 1, bdf3.striker[i])

plt.axvline(120, ls = '--', color = 'grey')
plt.axhline(60, ls = '--', color = 'grey')
plt.title("Best Batsman against R Ashwin", fontsize = 20)
plt.xlabel('Strike rate')
plt.ylabel('Runs scored')
plt.savefig('Chart_ABD_vs_Bumrah_part1.jpg')
plt.show()


# In[85]:


plt.figure(figsize = (16,8))
plt.rcParams['axes.facecolor'] = '#fff7fb'
plt.scatter(adf3.strike_rate, adf3.runs_off_bat)

for i in range(len(adf3)):
    if adf3.bowler[i] == 'R Ashwin':
        plt.text(adf3.strike_rate[i] + 2, adf3.runs_off_bat[i] - 1, adf3.bowler[i], color = 'maroon')
    elif (adf3.bowler[i] == 'RA Jadeja') | (adf3.bowler[i] == 'A Mishra') | (adf3.bowler[i] == 'PP Chawla') | (adf3.bowler[i] == 'Harbhajan Singh'):
        plt.text(adf3.strike_rate[i] + 2, adf3.runs_off_bat[i] - 1, adf3.bowler[i])
    elif (adf3.bowler[i] == 'SP Narine'):
        plt.text(adf3.strike_rate[i], adf3.runs_off_bat[i] + 2, adf3.bowler[i],color = 'maroon')
    elif (adf3.bowler[i] == 'Rashid Khan'):
        plt.text(adf3.strike_rate[i] - 3, adf3.runs_off_bat[i] - 3, adf3.bowler[i])

plt.axvline(110, ls = '--', color = 'grey')
plt.axhline(80, ls = '--', color = 'grey')
plt.title("Maxwell's Favorite Bowlers", fontsize = 20)
plt.xlabel('Strike rate')
plt.ylabel('Runs scored')
plt.savefig('Chart_Maxwell_vs_Ashwin_part2.jpg')
plt.show()


# In[129]:


plt.figure(figsize = (16,8))
plt.rcParams['axes.facecolor'] = '#fff7fb'
plt.scatter(bdf3.strike_rate, bdf3.runs_off_bat)

for i in range(len(bdf3)):
    if bdf3.striker[i] == 'PA Patel':
        plt.text(bdf3.strike_rate[i] - 7, bdf3.runs_off_bat[i] - 1, bdf3.striker[i])
    elif bdf3.striker[i] == 'BB McCullum':
        plt.text(bdf3.strike_rate[i] + 2, bdf3.runs_off_bat[i] - 1, bdf3.striker[i], color = 'maroon')
    elif (bdf3.striker[i] == 'S Dhawan') | (bdf3.striker[i] == 'CH Gayle') | (bdf3.striker[i] == 'DA Warner'):
        plt.text(bdf3.strike_rate[i] + 2, bdf3.runs_off_bat[i] - 1, bdf3.striker[i],color = 'maroon')
    elif (bdf3.striker[i] == 'DA Miller') | (bdf3.striker[i] == 'G Gambhir') | (bdf3.striker[i] == 'Yuvraj Singh'):
        plt.text(bdf3.strike_rate[i] + 2, bdf3.runs_off_bat[i] - 1, bdf3.striker[i],color = 'maroon')

plt.axvline(110, ls = '--', color = 'grey')
plt.axhline(60, ls = '--', color = 'grey')
plt.title(" R Ashwin's Favourite batsman", fontsize = 20)
plt.xlabel('Strike rate')
plt.ylabel('Runs scored')
plt.savefig('Chart_ABD_vs_Bumrah_part1.jpg')
plt.show()


# In[137]:


d=bdf3.sort_values('strike_rate', ascending = True)


# In[138]:


d.to_csv('Data_with_str.csv',index=None)

