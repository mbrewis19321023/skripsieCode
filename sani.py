#!/usr/bin/env python
# coding: utf-8

# In[1]:


flagForName = 0


import re
import random
import os
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pprint as pp

stdNumRegex = re.compile(r'_(\d{8}$)')
replaceList = re.compile(r"(\[')(\d{8})('\])")

def windowPop (title, message, typeofWindow):
    root = tk.Tk()
    root.withdraw()
    if typeofWindow == 'ask':
        return messagebox.askyesnocancel(title, message)
    elif typeofWindow == 'say':
        messagebox.showinfo(title, message)

# Goes through all the folders in the root directory and flags the existence of the needed folder
if 'sani.ipynb' in (os.listdir()):
    for filename in os.listdir():
        if filename == ('stdRepos'):
            flagForName = 1
    ################################################################################################################################################################# #################################################################################################################################################################

    # CODE MARK 1 # If the folder does not exist gicve the user the option to make the folder
    if flagForName == 0:
        answer = windowPop ("Warning", "There is no directory named 'stdRepos'! For the sanitation process to work the stdRepos folder must be in the same directory as the program. Would you like to create this directory?", 'ask')
        if answer == True:
            os.mkdir('stdRepos')
            windowPop("Note", "The folder 'stdRepos' has been created! Paste all unzipped student repositories to begin sanitation process and run this program again", 'say')
        else:
            pass
    #################################################################################################################################################################


if flagForName == True:
    try:
        os.chdir('stdRepos')
    except FileNotFoundError:
        windowPop("Note", 'Make sure that the program shares a parent directory with stdRepos' , 'say')

rg = re.compile(r'\d{8}')
listdir = os.listdir()
newList = list(filter(rg.findall, listdir))
newList


os.getcwd()

os.chdir('..')
try:
    import ds
    dictStd = ds.dictStd
except ModuleNotFoundError:
    print('ModuleNotFoundError')
os.chdir('stdRepos')

os.getcwd()

if newList:
    dictStd = {}
    listOfIndexes = []
    j = 0
    for i in os.listdir():
        listOfIndexes.append(j)
        j += 1


    random.shuffle(listOfIndexes)
    j = 0
    for i in os.listdir():
        dictStd.setdefault(replaceList.sub(r'\2', str(stdNumRegex.findall(i))), '#' + str(listOfIndexes[j]))
        j += 1
    
    os.chdir('..')
    fileObj = open('ds.py', 'w')
    fileObj.write('dictStd = ' + pp.pformat(dictStd) + '\n')
    fileObj.close()
    os.chdir('stdRepos')

try:
    df = pd.DataFrame(dictStd.items())
    df.rename(columns={0: "std", 1: "hsh"}, inplace = True)
except NameError:
    pass


if 'sani.ipynb' in os.listdir('..'):
    for x, i in enumerate (os.listdir()):
        try:
            os.rename(i, df.iloc[x][1])
        except FileExistsError:
            print("Already renamed")
        except NameError:
            print("The Data Frame has not been initilazed")

