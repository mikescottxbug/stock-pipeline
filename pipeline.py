import yfinance as yf #This line grabs a toolbox(library) "yfinance" from python that lets you oull data from yfinance
import pandas as pd #This line grabs a toolbox(library) "pandas" that lets you put numbers in a table

ticker_symbol = "MSFT" #Created a variable for the ticker we will use from yfinance

def extract(ticker_symbol): #created a function(recipe) to extract the ticker symbol
    data = yf.download(ticker_symbol, period = "10mo") #inside the function we call yfinances download funtion to download data from yahoo finance
    print(data) #this line prints data

extract(ticker_symbol) #this line ecalls the function