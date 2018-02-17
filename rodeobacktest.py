import pickle
import numpy as np
import random
import time
import datetime

try:
    import yapywrangler as yapy
except:
    print('The yahoo pynance module is not installed, please visit github.com/ltskinner/yapywrangler')
    exit()


#OK
class Trade(object):
    def __init__(self, buy, price, shares, day):
        self.buy = buy
        self.price = price
        self.shares = shares
        self.day = day