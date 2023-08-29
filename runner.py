from oanda_api import OandaAPI

api = OandaAPI()

while True:
    command = input("Enter command:  ")

    if command == "T":
        print("Making a Trade")
        trade_id = api.place_trade("EUR_USD", 100)
        print("trade_id", trade_id)
    elif command == "Q":
        print("Quitting")
        break
