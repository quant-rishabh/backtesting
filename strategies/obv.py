import pandas as pd
import numpy as np

pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)
def backtest(df : pd.DataFrame,ma_period:int):

    df['obv'] = (np.sign(df['close'].diff()) * df["volume"]).fillna(0).cumsum()
    df['obv_ma'] = round(df['obv'].rolling(window=ma_period).mean())

    df['signal'] = np.where(df['obv'] > df['obv_ma'], 1, -1)
    df['pnl'] = df['close'].pct_change() * df['signal'].shift(1)

    #cum
    print(df['pnl'].sum())