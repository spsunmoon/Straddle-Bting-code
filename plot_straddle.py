# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:05:38 2022

@author: spsid
"""
from mpl_toolkits import mplot3d
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates
from sklearn.preprocessing import LabelEncoder
import pandas as pd

BTdata = pd.read_csv('D:\\algo\\NIfty_data\\optBT.csv')


matrix= pd.DataFrame(columns=['Entry_time','Percentage','pnl'])
BTdata['Entry_date_time']= pd.to_datetime(BTdata['Entry_date_time'])
BTdata['Time'] = pd.to_datetime(BTdata['Entry_date_time']).dt.time



for i in range(9,15):
    for sl in range(1,10):
        stop_loss = (10/100)*sl
        entry_time =  datetime.time(i,20)
        t = BTdata[(BTdata['Time']== entry_time) & (BTdata['SL%']== stop_loss)]
        total = t['Total_pnl'].sum()
        matrix=matrix.append({'Entry_time':entry_time,
                                    'Percentage':stop_loss,
                                    'pnl':total},ignore_index=True)
        
matrix.to_csv(r'D:\\algo\\NIfty_data\\optimse.csv',index=None)

Final_data = matrix

x =Final_data['Entry_time']
y = []
z = []

for index,row in Final_data.iterrows():
    x.append(row['Entry_time'])
    y.append(row['Percentage'])
    z.append(row[ 'pnl'])
       




Final_data.iloc[0][0]
x = (Final_data.iloc[0][0])
y = Final_data.iloc[0][1]
z= Final_data.iloc[0][2]
ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Creating plot
ax.scatter3D(lbl['Percentage'], lbl['tim_sym'], lbl['pnl'], color = "green")
plt.title("simple 3D scatter plot")


le= LabelEncoder()
lbl = Final_data
lbl['tim_sym'] = le.fit_transform(lbl.Entry_time)
plt.scatter(lbl['tim_sym'],lbl['pnl'])
plt.scatter(lbl['Percentage'],lbl['pnl'])


import plotly.express as px
fig = px.scatter_3d(lbl, x='tim_sym', y='Percentage', z='pnl',
             )
fig.show()

                                    






