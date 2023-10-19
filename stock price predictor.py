import os
import time
import pandas_datareader as web
from winotify import Notification, audio

tickers = ["AAPL", "GS"]
upper_limits = [200, 320]
lower_limits = [130, 260]

while True:
    last_prices = [web.DataReader(ticker, "yahoo")["Adj Close"][-1] for ticker in tickers]
    print(last_prices)
    time.sleep(10)

    for i in range(len(tickers)):
        if last_prices[i] > upper_limits[i]:
            toast = Notification(title="price alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]} you might want to sell")
            toast.add_actions(label="go to stockbroker", launch="https://kite.zerodha.com/")
            toast.set_audio(audio.LoopingAlarm6)
            toast.show()
        elif last_prices[i] < lower_limits[i]:
            toast = Notification(title="price alert for " + tickers[i],
                                 msg=f"{tickers[i]} has reached a price of {last_prices[i]} you might want to Buy")
            toast.add_actions(label="go to stockbroker", launch="https://kite.zerodha.com/")
            toast.set_audio(audio.LoopingAlarm8)
            toast.show()

        time.sleep(5)
