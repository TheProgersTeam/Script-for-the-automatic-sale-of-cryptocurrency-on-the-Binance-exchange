#!/usr/bin/env python3
# Connecting to Binance Api
# pip install python-binance
from binance.client import Client
from binance.websockets import BinanceSocketManager
# Working with time 
from time import sleep
# Working with calculations
import math

# Api key
api_key = '...'
# Secret key
api_secret = '...'
# Client
client = Client(api_key, api_secret)


# Market in which we trade (Name of cryptocurrency + Name of fiat currency)
ASSET = 'BTCUSDT'
# Currency name
CURRENCY = 'USDT'
# Cryptocurrency name
CRYPTOCURRENCY = 'BTC'
# The time period between receiving a new price
TIME_SLEEP = 5
# Fall percentage at which the sale will be made
Percent = -15


# Wallet balance
def balance(symbol):
    balance = client.get_asset_balance(asset=symbol)
    balance = {'free': balance['free'], 'locked':balance['locked']}
    return balance
 
# Cryptocurrency price
def price(symbol):
    price = client.get_avg_price(symbol=symbol)['price']
    return float(price)

# Selling cryptocurrency
def order_market_sell(quantity):
    client.order_market_sell(symbol=ASSET, quantity=quantity)

# The function truncates the number to the n'th number of characters (It is necessary so that there are no errors during buying and selling)
def toFixed(f: float, n=0):
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

# Endless cycle
BEST_PRICE = float(price(ASSET))
while True:
    # Temporary delay
    sleep(TIME_SLEEP)
    
    PRICE = float(price(ASSET))
 
    if PRICE >= BEST_PRICE:
        BEST_PRICE = PRICE
        
    # Calculate the percentage of change
    percentage_of_change = ((PRICE - BEST_PRICE) / BEST_PRICE) * 100

    print('Best price:', str(BEST_PRICE), '| New price:', str(PRICE), '| Change:', str(percentage_of_change), '\n')

    if percentage_of_change <= Percent:
        order_market_sell(toFixed(float(balance(CRYPTOCURRENCY)['free']), 6))
        # Stop the cycle
        break
        
