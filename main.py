import logging

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
    mode = input("choose  the program mode (data/ backtest / optimize)").lower()
    



