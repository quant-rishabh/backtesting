import pandas as pd

def pnl(df : pd.DataFrame):
    df['pnl'] = df['close'].pct_change() * df['signal'].shift(1)
