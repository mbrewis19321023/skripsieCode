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

# begin setting of home path variable and adding data directory to path import list
if 'Step_1.ipynb' or 'Step_1.py' or 'Step_1.exe' in os.listdir():
    home = os.getcwd()     
sys.path.append(os.path.join(home, 'data')) #This will add the data folder to the path variable so modules can be imported 
# end setting of home path variable and adding data directory to path import list

# begin creation Regular Expressions
validHash = re.compile(r'#\d{0,3}')

pinRegex1 = re.compile(r'GPIO_InitStruct.Pin\s*=\s*')
pinRegex2 = re.compile(r'(\w+)')


modeRegex = re.compile(r'''
            GPIO_MODE_                  #This will match the first part
            (
            INPUT|
            OUTPUT_PP|
            OUTPUT_OD|
            AF_PP|
            AF_OD|
            ANALOG|
            IT_RISING|
            IT_FALLING|
            IT_RISING_FALLING|
            EVT_RISING|
            EVT_FALLING|
            EVT_RISING_FALLING)    
            ''', re.VERBOSE)

pullRegex = re.compile(r'''
            GPIO_NOPULL|
            GPIO_PULLUP|
            GPIO_PULLDOWN
            ''', re.VERBOSE)

speedRegex = re.compile(r'''
             GPIO_SPEED_FREQ_LOW|
             GPIO_SPEED_FREQ_MEDIUM|
             GPIO_SPEED_FREQ_HIGH|
             GPIO_SPEED_FREQ_VERY_HIGH
             ''', re.VERBOSE)

gpioInitRegex = re.compile(r'''
                 HAL_GPIO_Init\((\w+),
                 ''', re.VERBOSE)
# end creation Regular Expressions

# begin import of created modules
try:   
    import ds
    import mypath
except ModuleNotFoundError:
   pass
# begin import of created modules

# begin importing and creation of a data frame
os.chdir(mypath.data)
df = pd.read_csv('data.csv')
# end importing and creation of a data frame

pd.set_option('max_colwidth', 200)
df


# In[2]:


# begin adding a path to main.c column to dataframe
df['main.c Path'] = 'No main.c file. Double check student repository for correct upload!'
# end adding a path to main.c column to dataframe

# begin function that identifies the pinout in main.c
def goIntoMain(pathToC, i):
    try:
        cfile = open(pathToC)
    except FileNotFoundError:
        df.loc[df['hsh'] == i, 'main.c Path'] = 'No main.c file. Double check student repository for correct upload!'
        pass
# end function that identifies the pinout in main.c

# begin looping through each student repo to find the main.c file and pass it to the function that goes into main and gets the pinouts
os.chdir(mypath.repos)
for i in os.listdir():
#     import ipdb; ipdb.set_trace()
    pathToCore = df.loc[df['hsh'] == i, 'CorePath'].values[0]
    if os.path.isdir(pathToCore):
        pathToCFile = os.path.join(pathToCore, 'Src', 'main.c')
        df.loc[df['hsh'] == i, 'main.c Path'] = pathToCFile
        goIntoMain(pathToCFile , i)
    else:
        pass
os.chdir(mypath.repos)
# end looping through each student repo to find the main.c file and pass it to the function that goes into main and gets the pinouts


# In[3]:


def makePins(testGoMain, j):   
    
    dfPins = pd.DataFrame(columns = ['Port', 'Pin', 'Mode','Pull-Type','Speed']) 
    
    try:
        cFileT = open(testGoMain) 
        lines = cFileT.readlines() 
    except FileNotFoundError:
        dfPins.to_csv(j + '.csv', index = False)
        lines = 'Empty repo'
        dfPins.loc[1] = lines

        
    
#     os.chdir(mypath.data)
#     cFileT = open('test.c') 
#     lines = cFileT.readlines()  
          
   
    pinList = []
    validList = []
    modeList = []
    pullList = []
    speedList = []
    x = 0

    for i in lines:
#         import ipdb; ipdb.set_trace()
        isValid = pinRegex1.findall(i)
        isPinLine = pinRegex2.findall(i)
        isModeLine = modeRegex.findall(i)
        isPullLine = pullRegex.findall(i)
        isSpeedLine = speedRegex.findall(i)
        isGpioInitLine = gpioInitRegex.findall(i)
        if isPinLine and isValid:
            pinList.extend(isPinLine[2:])
            validList.extend(isValid)      
        elif isModeLine:
            modeList.extend(isModeLine)
        elif isPullLine:
            pullList.extend(isPullLine)
        elif isSpeedLine:
            speedList.extend(isSpeedLine)
        elif isGpioInitLine and pinList and validList:
            dfTempPin = pd.DataFrame(columns = ['Port', 'Pin', 'Mode','Pull-Type','Speed']) 
            for i in pinList:
                dfPins.loc[x] = [isGpioInitLine[0]] +  [i] + [modeList] + [pullList] + [speedList]
                x += 1           
            pinList = []
            modeList = []
            pullList = []
            speedList = []
            validList = []
        else:
            pass
    
    os.chdir(mypath.data)
    dfPins.to_csv(j + '.csv', index = False)

    


# In[4]:


os.chdir(mypath.repos)
for i in os.listdir():  
#     import ipdb; ipdb.set_trace()
    testGoMain = df.loc[df['hsh'] == i, 'main.c Path'].values[0]
    makePins(testGoMain, i)


# In[5]:


# # This is the regulkar exppressions needed to solve the bug of B1_Pin
# pinRegex2 = re.compile(r'GPIO_InitStruct.Pin\s*=\s*')
# testRegex2 = re.compile(r'(\w+)')
# string = 'GPIO_InitStruct.Pin = GPIO_PIN_6|GPIO_PIN_7|GPIO_PIN_8|GPIO_PIN_10'
# string2 = pinRegex2.split(string)[1]
# testRegex2.findall(string2)

