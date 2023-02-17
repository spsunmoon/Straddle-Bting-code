# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:44:50 2022

@author: spsid
##options backtest

"""
##df = pd.read_parquet('C://Users//spsid//Downloads//Telegram Desktop//NFO_19_Sep_2022_From_AliceBlue.parquet')
##new_df = df[df['Symbol'].str.contains('BANKNIFTY')] 
##df.to_csv('filename.csv')

import pandas as pd
import numpy as np  
import datetime
from glob import glob
from dateutil.relativedelta import relativedelta,TH

loc = pd.DataFrame(glob("D:/algo/NIfty_data/options sample data/sample_data_Jan2019/*"),columns=['loc'])
loc['date'] = loc['loc'].apply(lambda x: x.split('_')[-1].split('.')[0])

for index , row in loc.iterrows():
    entrytime = '09:20:00'
    data=pd.read_pickle(row['loc'])
    instrument = 'BANKNIFTY'
    data['exp_type'] = np.where((data['instrument_type']=="FUT"),(data['ticker'].apply(lambda x: x.split('-')[-1].split('.')[0])),"")
    data_FUT= data[(data['instrument_name']==instrument) & (data['instrument_type']=='FUT') & ( data['exp_type'] == 'I') ]
    atm = data_FUT[data_FUT['time'] == entrytime]['open'].iloc[0]
    

test_date = datetime.datetime(2019, 3, 23), weekday_idx = 3 


