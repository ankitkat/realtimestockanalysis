#Realitime stock analysis using yahoo_fin library. Below code will provide analysis for last three days of stock performance.
from datetime import datetime, timedelta
import yahoo_fin.stock_info as si
listx = ["aapl","gsk","ge","abt","abbv","afl"]
stdate = datetime.today() - timedelta(days=3)
enddate = datetime.today()
for i in range(len(listx)):
        print("Today's date:", enddate)
        print(listx[i])
        print ('My Stock :', listx[i])
        print('Live Price :',si.get_live_price(listx[i]))
        print("----------------------------------------------------------------------")
        print(si.get_quote_table(listx[i], dict_result = False))
        print("----------------------------------------------------------------------")
        print(si.get_data(listx[i], start_date = stdate, end_date = enddate))
        print("----------------------------------------------------------------------")
        
 #------------------------------------------------------------------------------------------------------------------------------------------
 #save as txt file - To save above mentioned analysis as TXT use below mentioned code
from datetime import datetime, timedelta
import os
import sys
sys.stdout = open("test1.txt", "w")
import yahoo_fin.stock_info as si
import pandas as pd
import csv
listx = ["aapl","gsk","ge","abt","abbv","afl"]
stdate = datetime.today() - timedelta(days=3)
enddate = datetime.today()
for i in range(len(listx)):
        print(listx[i])
        print ('My Stoke :', listx[i])
        print('Live Price :',si.get_live_price(listx[i]))
        print("----------------------------------------------------------------------")
        print(si.get_quote_table(listx[i], dict_result = False))
        print("----------------------------------------------------------------------")
        print(si.get_data(listx[i], start_date = stdate, end_date = enddate))
        print("----------------------------------------------------------------------")
sys.stdout.close()
TEST1.TXT
