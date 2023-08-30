import pandas as pd

from defs import BUY, SELL, NONE

class Technicals():

    def __init__(self, settings, api, pair, granularity, log=None):
        self.settings = settings
        self.log = log
        self.api = api
        self.pair = pair
        self.granularity = granularity

    def log_message(self, msg):
        if self.log is not None:
            self.log.logger.debug(msg)

    def fetch_candles(self, row_count, candle_time):
        status_code, df = self.api.fetch_candles(self.pair, count=row_count, granularity=self.granularity)
        if df is None:
            self.log(f"Error fetching candles for pair{self.pair} {candle_time}, df None")
            return None
        elif df.iloc[-1].time != candle_time:
            self.log_message(f"Error fetching candles for pair: {self.pair} {candle_time} vs {df.iloc[-1].time}")
            return None
        else:
            return df
        
    def process_candles(self, df):
        pass

    def get_trade_decision(self, candle_time):
        max_rows = self.settings.long_ma + 2
        self.log_message("")
        self.log(f"get_trade_decision() pair: {self.pair} max_rows: {max_rows}")

        df = self.fetch_candles(max_rows, candle_time)
        if df is not None:
            return self.process_candles(df)
        return None

