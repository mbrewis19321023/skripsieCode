#!/usr/bin/env python
# coding: utf-8

# In[1]:


# begin importing of standard modules
import re
import random
import os
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pprint as pp
import sys
# end importing of standard modules

##############################################################################################################################################################################################################################

# begin setting of home path variable and adding data directory to path import list
if 'sani.ipynb' or 'sani.py' in os.listdir():
    home = os.getcwd()     
sys.path.append(os.path.join(home, 'data')) #This will add the data folder to the path variable so modules can be imported 
# end setting of home path variable and adding data directory to path import list

##############################################################################################################################################################################################################################

# begin import of created modules
try:   
    import ds
    import mypath
    input('''Success!!!

Press any key to exit...''')
except ModuleNotFoundError:
    input('''Before this program can be run, sani.py must be run first.
This will ensure that the needed python modules are created in the data directory!

Please run sani.py and try again

Press any key to exit...''')
# begin import of created modules

##############################################################################################################################################################################################################################


# In[2]:


# begin importing and creation of a data frame
df = pd.DataFrame(ds.dictStd.items())
df.rename(columns={0: "std", 1: "hsh"}, inplace = True)
# end importing and creation of a data frame

##############################################################################################################################################################################################################################

# begin vreation of the drivers path column in dataDrame
df['DriversPath'] = 'NaN'
# end vreation of the drivers path column in dataDrame

##############################################################################################################################################################################################################################


# In[3]:


validHash = re.compile(r'#\d{0,3}')


# In[4]:


# def findDriver(pathOfFile):
#     import ipdb; ipdb.set_trace()
#     os.chdir(pathOfFile)
#     if 'Drivers' in os.listdir():
#         df.loc[df['hsh'] == validHash.findall(os.getcwd())[0], ['DriversPath']] = os.path.join(os.getcwd(), pathOfFile)
#         os.chdir(mypath.repos)
#     else:
#         for i in os.listdir():
#             if os.path.isdir(i):
#                 pathOfFile = os.path.join(os.getcwd() ,  str(i))
#                 findDriver(pathOfFile)
#             else:
#                 os.chdir(mypath.repos)


# In[5]:


def findDrivers2(filepath):
#     import ipdb; ipdb.set_trace()
    for i in os.listdir(filepath):
        newPath = os.path.join(filepath , i)
        if i in ['.git','.settings','Core','Debug','.metadata']:
            pass
        elif i == 'Drivers':
            df.loc[df['hsh'] == validHash.findall(newPath)[0], ['DriversPath']] = newPath
        elif os.path.isdir(newPath) == False:
            pass
        elif os.path.isdir(newPath) and i != 'Drivers':                   
            findDrivers2(newPath)


# In[6]:


os.chdir(mypath.repos)
os.getcwd()
os.listdir()
# findDriver(mypath.repos)
filepath = mypath.repos
findDrivers2(filepath)


# In[7]:


# for i in range(6):
#     import ipdb; ipdb.set_trace()
#     print(i)


# In[8]:


# os.chdir(os.path.join(mypath.repos , str('#1')))
# for i in os.listdir():
#     if os.path.isdir(i):
#         print('yes')
# os.listdir()


# In[9]:


pd.set_option('max_colwidth', 200)


# In[10]:


df

