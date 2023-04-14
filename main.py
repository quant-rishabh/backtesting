import logging
from exchange.binance import BinanceClient
from data_collector import collect_all
import backtester
import datetime
from utils import TF_EQUIV
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(levelname)s :: %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler("info.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)


logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# logger.info("this a info log")


# only this file run then only run otherwise if imported in other then dont run

if __name__ == "__main__":
    mode = input("choose  the program mode (data/ backtest / optimize) : ").lower()
    client = BinanceClient()
    while True:
        exchange = input("Choose a exchange : ")
        if exchange == "binance":
            break


    while True:
        symbol = input("Choose a symbol : ").upper()
        if symbol in client.symbols:
            break

    if mode == "data":
        collect_all(client, exchange, symbol)


    elif mode == "backtest":

        #strategy testing


        available_strategies =['obv']
        while True:
            strategy = input(f"Chose a strategy: ({', '.join(available_strategies)}) : ").lower()

            if strategy in available_strategies:
                break
        #timeframe
        while True:
            tf = input(f"Chose a timeframe: ({', '.join(TF_EQUIV.keys())}): ").lower()

            if tf in TF_EQUIV.keys():
                break
         #from_time
        while True:
            from_time = input("backtest from (yyyy-mm-dd or Press Enter): ")

            if from_time == "":
                from_time = 0
                break
            try:
                from_time = int(datetime.datetime.strptime(from_time,"%y-%m-%d").timestamp()*1000)
                break
            except ValueError:
                continue

        # to Time
        while True:
            to_time = input("backtest to (yyyy-mm-dd or Press Enter) : ")

            if to_time == "":
                to_time = int(datetime.datetime.now().timestamp()*1000)
                break
            try:
                to_time = int(datetime.datetime.strptime(to_time, "%y-%m-%d").timestamp() * 1000)
                break
            except ValueError:
                continue


        backtester.run(exchange,symbol,strategy, tf, from_time,to_time)


