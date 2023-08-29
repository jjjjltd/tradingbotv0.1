from oanda_api import OandaAPI

api = OandaAPI()

while True:
    command = input("Enter command:  ")

    if command == "T":
        trade_id = api.place_trade("EUR_USD", 100, take_profit=1.096, stop_loss=1.072)
        print("trade_id", trade_id)
    elif command == "Q":

        break
