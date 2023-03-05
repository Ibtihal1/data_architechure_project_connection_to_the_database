#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:55:36 2021

@author: ibtihalkhan
"""
import psycopg2
import pandas as pd

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='ibtihalkhan', password='', host='127.0.0.1', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
cursor.execute('''SELECT * from boston_crime''')


#Fetching all row from the table
result = cursor.fetchall();
df = pd.DataFrame(result,columns=('incident_number','offense_code','offense_code_group', 'offense_description', 'district, reporting_area', 'shooting', 'occurred_on_date', 'year',' month', 'day_of_week', 'hour', 'ucr_part', 'street', 'lat', 'long', 'location'," "))
print(df)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()

