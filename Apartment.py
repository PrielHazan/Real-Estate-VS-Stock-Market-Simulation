import logging
# logging.basicConfig(level=logging.DEBUG)
class Apartment:
    def __init__(self, money, yieldPerYear, growthPerYear, addRentToVal):
        self.year = 1
        self.apartmentVal = money
        self.totalMoney = money
        self.yieldPerYear = yieldPerYear
        self.growthPerYear = growthPerYear
        self.landAppreciation = 0
        self.addRentToVal = addRentToVal
        self.rentMoneyTax = 10
        self.landAppreciationTax = 25

    def NextYear(self):
        logging.debug(f"year number {self.year} :::")
        self.year += 1
        rentMoney = self.apartmentVal *(float(self.yieldPerYear)/100)
        # rent tax
        rentMoney *= (1-self.rentMoneyTax/100)
        logging.debug(f"{rentMoney=}")
        addedToApartmentVal = self.apartmentVal * (float(self.growthPerYear)/100)
        logging.debug(f"{addedToApartmentVal=}")
        self.apartmentVal += addedToApartmentVal
        self.landAppreciation += addedToApartmentVal
        if (self.addRentToVal):
            self.apartmentVal += rentMoney
            self.totalMoney = self.apartmentVal
        else:
            self.totalMoney += addedToApartmentVal + rentMoney
        logging.debug(f"{self.apartmentVal=}")
        logging.debug(f"{self.totalMoney=}")
        logging.debug(f"{self.totalValue()=}")
        logging.debug("\n\n")
        return self.totalValue()
    def totalValue(self):
        return self.totalMoney - self.landAppreciation*(self.landAppreciationTax/100)
