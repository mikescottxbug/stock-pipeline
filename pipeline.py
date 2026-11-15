import yfinance as yf #Grabbing toolbox: yfinance, and call it yf for short
import pandas as pd #Grabbing toolbox: pandas, and call it pd for short; handles data tables

ticker_symbol = "AAPL" #Make a labeled box called ticker_symbol abd out the text AAPL in it. 

def extract(ticker_symbol): #heres a recipe called extract. it needs one ingredient, a ticker
    data = yf.download(ticker_symbol, period= "5d") #yf.download is a tool in toolbox yf.
    print(data)

extract(ticker_symbol)
