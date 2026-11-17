import yfinance as yf #This line grabs a toolbox(library) "yfinance" from python that lets you oull data from yfinance
import pandas as pd #This line grabs a toolbox(library) "pandas" that lets you put numbers in a table

ticker_symbol = "MSFT" #Created a variable for the ticker we will use from yfinance

def extract(ticker_symbol): #created a function(recipe) to extract the ticker symbol
    data = yf.download(ticker_symbol, period = "10mo") #inside the function we call yfinances download funtion to download data from yahoo finance
    return data

raw_data = extract(ticker_symbol)
raw_data.columns = raw_data.columns.droplevel(1)
raw_data = raw_data.reset_index()
raw_data.columns = raw_data.columns.str.lower()
raw_data = raw_data.dropna()
print(raw_data.tail())