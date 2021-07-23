import logging
# logging.basicConfig(level=logging.DEBUG)
class Stocks:
    def __init__(self, money, yieldPerYear, exchangeTax):
        self.year = 1
        self.exchangeTax = exchangeTax
        self.stocksVal = money * (1-exchangeTax/100)
        self.yieldPerYear = yieldPerYear
        self.totalProfit = 0
        self.profitTax = 25

    def NextYear(self):
        logging.debug(f"year number {self.year} :::")
        self.year += 1
        profit = self.stocksVal * (self.yieldPerYear/100)
        self.stocksVal += profit
        self.totalProfit += profit

        logging.debug(f"{profit=}")
        logging.debug(f"{self.totalProfit=}")
        logging.debug(f"{self.stocksVal=}")
        logging.debug(f"{self.totalValue()=}")
        logging.debug("\n\n")
        return self.totalValue()
    def totalValue(self):
        # dollar to shekel tax
        stocksValAfterExchange = self.stocksVal * (1-self.exchangeTax/100)
        return stocksValAfterExchange - self.totalProfit*(self.profitTax/100)
