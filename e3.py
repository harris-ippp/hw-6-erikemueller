import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#create dataframe
dataframe = []
#open from ELECTION_ID file
file = open('ELECTION_ID', 'r')
#align files with years
for line in file.readlines():
    source = line.split()
    year = source[0]+".csv"
#read csvs
    header = pd.read_csv(year, nrows = 1).dropna(axis = 1)
#send data to dataframe
    d = header.iloc[0].to_dict()
#send data from csv to dataframe
    df = pd.read_csv(year, index_col = 0, thousands = ",", skiprows = [1])
#keep names
    df.rename(inplace = True, columns = d)
#remove na values
    df.dropna(inplace = True, axis = 1)
    df["Year"] = source[0]
    #name frames
    dataframe.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
#take dataframe and use concat to put all data into all
    all = pd.concat(dataframe)
    #find proportion republican
    all["Republican Share"] = all["Republican"]/all["Total Votes Cast"]
#set proportion for each county and city
#for some reason sort_values doesn't work here
#get this error TypeError: sort_values() got an unexpected keyword argument 'by'
    accomack = all.loc['Accomack County'].astype(float)
    albemarle = all.loc['Albemarle County'].astype(float)
    alexandria = all.loc['Alexandria City'].astype(float)
    alleghany = all.loc['Alleghany County'].astype(float)
#create graphs
    graph1 = accomack.plot(kind = "line", x = "Year" ,y = "Republican Share")
    graph1.get_figure().savefig('accomack_county.pdf')
    graph2 = albemarle.plot(kind = "line", x = "Year" ,y = "Republican Share")
    graph2.get_figure().savefig('albemarle_county.pdf')
    graph3 = alexandria.plot(kind = "line", x = "Year" ,y = "Republican Share")
    graph3.get_figure().savefig('alexandria_city.pdf')
    graph4 = alleghany.plot(kind = "line", x = "Year" ,y = "Republican Share")
    graph4.get_figure().savefig('alleghany_county.pdf')
