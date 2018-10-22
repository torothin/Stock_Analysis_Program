
# coding: utf-8
import requests, pandas
from bs4 import BeautifulSoup
from datetime import datetime as dt
import time

host_path="https://finance.yahoo.com/quote/AAPL?p=AAPL"
ticker_name=host_path[len(host_path)-4:]

i=7
while i<=13:
    j=0
    while j==0 or j==30:
        l=[]
        l2=["Time", "Price"]
        date_Today=dt.now()
        date_String=date_Today.strftime("%m-%d-%y-%H-%M")
        end_time=dt(dt.now().year, dt.now().month, dt.now().day,i,j)

        while dt.now()<end_time:
            r=requests.get(host_path)
            c=r.content
            soup=BeautifulSoup(c,"html.parser")
            all=soup.find_all("div",{"class":"D(ib) Fw(200) Mend(20px)"})
            time_Now=dt.now().strftime("%H-%M-%S")
            price=all[0].find("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
            l.append([time_Now,price])
        j+=1
        if j==1: j=30
        df=pandas.DataFrame(l,columns=l2)
        df.index.name = ticker_name
        df.to_csv("Yahoo_{}_{}.csv".format(ticker_name,date_String))

    i+=1
