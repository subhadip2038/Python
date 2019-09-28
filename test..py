# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:40:58 2019

@author: subha
"""

#Question 1 - Which type of complaints should the Department of Housing Preservation and Development of New York City focus on first?

#import all the libraries required for solving the question.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import the data from local file fhrw-4uyv.csv

data = pd.read_csv("https://data.cityofnewyork.us/resource/fhrw-4uyv.csv?$limit=100000000&Agency=HPD&$select=created_date,unique_key,complaint_type,incident_zip,incident_address,street_name,address_type,city,resolution_description,borough,latitude,longitude,closed_date,location_type,status")
data.head()
# Trancate the data 
ct_data = pd.DataFrame(data, columns = ['complaint_type','unique_key'])
# Group By Complaint type
count= ct_data.groupby(by= ['complaint_type']).count()
# Data Visualization
count.plot(kind='bar')

plt.title("Complaint Type in New York 311")
plt.xlable('Complaint Type')
plt.ylable('Count of Unique key')
