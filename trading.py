import alpaca_trade_api as tradeapi
class Trading(object):
    def __init__(self):
        self.key = '*************'  #enter your own secret key
        self.secret = '*******************'   #enter your own secret 
        self.aplaca_endpoint = 'https://paper-api.alpaca.markets'
        self.api = tradeapi.REST(self.key, self.secret, self.aplaca_endpoint)
        self.symbol = input("Enter stock symbol: ")
        if self.symbol.islower():
            self.symbol= self.symbol.upper()
        self.newOrder = None
        self.last_price = 1
        try:
            self.position = int(self.api.get_position(self.symbol).qty)
        except:
            self.position = 0
    def submit_order(self, target):
        if not(self.newOrder is None):
            self.api.cancel_order(self.newOrder.id)

        newBalance = target - self.position
        if newBalance == 0:
            return
        print(f"processing the order for {target} shares of " + self.symbol)

        if newBalance > 0: 
            quant = newBalance
            if self.position <0:
                quant = min(abs(self.position), quant)
            print(f"Buying {quant} shares of " + self.symbol)
            self.newOrder = self. api.submit_order(self.symbol,quant,'buy','limit','day',self.last_price)
            print(self.last_price)
            print(f"Bought 3 shares of "+ self.symbol) 

        elif newBalance <0:
            self_quantity = abs(newBalance)
            if self.position>0:
                ammounToSell=min(abs(self.position), ammounToSell)
            print(f"selling {ammounToSell} shares")
            self.newOrder = self.api.submit_order(self.symbol,ammounToSell,"sell","limit","day",self.last_price)
if __name__  == "__main__":
    t = Trading()
    t.submit_order(3)