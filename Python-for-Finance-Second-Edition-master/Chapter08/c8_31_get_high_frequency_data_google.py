"""
  Name     : c8_31_get_high_fequency_data_google.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import re, string 
import pandas as pd 
ticker='AAPL'                        # input a ticker 
f1="c:/temp/ttt.txt"               # ttt will be replace with above sticker
f2=f1.replace("ttt",ticker) 
outfile=open(f2,"w") 
path="https://www.google.com/finance/getprices?q=ttt&i=300&p=10d&f=d,o,%20h,l,c,v"
path2=path.replace("ttt",ticker) 
df=pd.read_csv(path2,skiprows=8,header=None) 
df.to_csv(outfile,header=False,index=False) 
outfile.close() 
