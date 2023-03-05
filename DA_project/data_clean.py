A#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:11:45 2021

@author: ibtihalkhan
"""

import pandas as pd
import numpy as np
import datetime

#read crime dataset
boston_crime = pd.read_csv("/Users/ibtihalkhan/Downloads/crime.csv", encoding = "latin1",low_memory=False)
boston_crime.info()

#print no of nan value 
print(boston_crime.isnull().sum(), end = '\n\n')

print("\n\nTotal duplicate data in the dataset\n")
print(boston_crime.duplicated().sum())
#df = boston_crime[boston_crime.duplicated(subset=['INCIDENT_NUMBER','OFFENSE_CODE'], keep=False)]
print("\n\n Duplicate data in the dataset\n")
duplicateDFRow = boston_crime[boston_crime.duplicated()]
print(duplicateDFRow)


#cleaning the data

# convert the Occurred_On_Date feature from datetime to date
boston_crime["OCCURRED_ON_DATE"] = boston_crime["OCCURRED_ON_DATE"].apply(pd.to_datetime, errors='coerce')
boston_crime["OCCURRED_ON_DATE"] = boston_crime["OCCURRED_ON_DATE"].dt.date
#fill N in the Shooting column,assume nulls were not shooting.
boston_crime.SHOOTING.fillna('N', inplace=True)
#removed the remaining Null/NaN values as it is small part of the crime data set
boston_crime=boston_crime.dropna()
#drop duplicates in the dataset
boston_crime=boston_crime.drop_duplicates()
#replace " " in reporting_area to 0 means not known
boston_crime=boston_crime.replace(to_replace = " ", value =0)
boston_crime

boston_crime.to_csv(r'/Users/ibtihalkhan/Downloads\BOSTON_CRIME.csv', index = False)
