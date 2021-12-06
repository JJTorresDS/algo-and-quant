# -*- coding: utf-8 -*-
"""
Script to import data from yahoo finance
"""

import datetime
import yfinance as yf
import pandas as pd


stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS"]
start = datetime.datetime.today() - datetime.timedelta(30)
e