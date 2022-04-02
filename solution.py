# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:54:30 2022

@author: MinHyeok
"""
from datetime import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
'''
Issurance Date: a string prefixed with "DIs"
CleanBid: a number prefixed with BPr
CleanAsk: a number prefixed with APl
LastPrice: a number prfefixed with Pl
'''
'''
lst: one line splitted in to a list with (";")
prefix: prefix of each information that we want to extract
returns: list of string containing the prefix
'''
def filter_line(lst, prefix):
    f = filter(lambda x: prefix in x, lst)
    return list(f)


'''
iterates through the file and for each record(10 lines)
issurance date is saved in the 7th line of record
CleanBid, CleanAsk, LastPrice are saved in the 10th line of record.
Note that some record might not have CleanBid, CleanAsk, and LastPrice.
'''
def organize_in_dictionary(file):
    with open(file) as f:
        lines = f.readlines()

    dic = {}
    for i in range(0, len(lines), 10):
        #get Issurance Date
        i += 6
        issurance_date = filter_line(lines[i].split(";"), "DIs")
        issurance_date = issurance_date[0][3:]
        
        #this part is to add more dictionary value if the date appears more than once
        if (dic.get(issurance_date, False)== False):
            dic[issurance_date] = [{}]
        elif (dic.get(issurance_date, False) != False):
            dic[issurance_date].append({})
        
        #note: dic[issurance_date][-1] is used to keep track of newly added dictionary from above.   
        i+=3
        #get CleanBid
        clean_bid = filter_line(lines[i].split(";"), "BPr")
        if len(clean_bid) != 0:
            dic[issurance_date][-1]["CleanBid"] = float(clean_bid[0][3:])    
            
        #get CleanAsk and LastPrice
        #result contains both CleanAsk, LastPrice or one of them or None.
        result = filter_line(lines[i].split(";"), "Pl")
        if (len(result) == 1): #Pl 
            dic[issurance_date][-1]["LastPrice"] = float(result[0][2:])   
        elif (len(result) == 2): #both APl or Pl
            dic[issurance_date][-1]["CleanAsk"] = float(result[0][3:])
            dic[issurance_date][-1]["LastPrice"] = float(result[1][2:])
    return dic

'''
Plot the CleanBid(blue), Clean Ask(red), LastPrice(green) on the pyplot and save
the result image.
'''
def plot(dic):
    plt.figure()
    ax = plt.gca()
    date_format = mdates.DateFormatter('%Y%m%d')
    ax.xaxis.set_major_formatter(date_format)
    for k, v in dic.items():
        x = dt.strptime(k, "%Y%m%d")
        x = mdates.date2num(x)
        for val in v:
            cb = val.get("CleanBid", False)
            ca = val.get("CleanAsk", False)
            lp = val.get("LastPrice", False)
            if cb != False:
                plt.plot_date(x, cb, 'bo', markersize=8, xdate=True)
            if ca != False:
                plt.plot_date(x, ca, 'ro',markersize= 4,  xdate=True)
            if lp != False:
                plt.plot_date(x, lp, 'go', markersize=2,  xdate=True)
    plt.savefig("result.jpg")
    
    
if __name__ == "__main__":
    dic = organize_in_dictionary("XICE_Bond_Close2.tip")
    plot(dic)
    