class Market(object):
    def __init__(self):
        self.asks = []
        self.bids = []
        self.transactions = []

    def bid(self, price, volume=1):
        if len(self.asks) > 0:
            asks_pop = self.asks.pop(0)
            self.transactions.append(((price, volume), asks_pop))
        else:
            self.bids.append((price, volume))

    def ask(self, price, volume=1):
        if len(self.bids) > 0:
            bids_pop = self.bids.pop(0)
            self.transactions.append((bids_pop, (price, volume)))
        else:
            self.asks.append((price, volume))
