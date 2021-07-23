from Apartment import Apartment
from Stocks import Stocks
import logging
# logging.basicConfig(level=logging.DEBUG)
from matplotlib import pyplot as plt


def Average(lst):
    return sum(lst) / len(lst)


startingMoney = 1000000
years = 10


# stocks
stocks_money_y = []
MicrosoftYieldPast4Years = [40.34, 19.16, 55.62, 40.13]
GoogleYieldPast4Years = [32.93, -0.64, 30.08, 28.02]
# print(Average(MicrosoftYieldPast4Years))
# print(Average(GoogleYieldPast4Years))
stocksYieldPerYear = (Average(MicrosoftYieldPast4Years) + Average(GoogleYieldPast4Years))/2
logging.debug(f"{stocksYieldPerYear=}\n")
exchangeTax = 1
stocks = Stocks(startingMoney, stocksYieldPerYear, exchangeTax)
for _ in range(years):
    stocks_money_y.append(stocks.NextYear())


# real Estate
apartment_money_y = []
yieldPerYear = 4
growthPerYear = 5
addRentToVal = True
apartment = Apartment(startingMoney, yieldPerYear, growthPerYear, addRentToVal)
for _ in range(years):
    apartment_money_y.append(apartment.NextYear())

print(apartment_money_y)
print(stocks_money_y)

# plt.xkcd()

years_x = [year + 2022 for year in range(years)]


plt.plot(years_x, stocks_money_y, linestyle='--', label='Stocks Total Money')


plt.plot(years_x, apartment_money_y, label='Apartment Total Money')

# plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')

plt.xlabel('years')
plt.ylabel('Total Money (SHEKELS)')
plt.title('Stocks VS real Estate')

plt.legend()

plt.tight_layout()

plt.savefig('stocksVSrealEstate.png')

plt.show()
