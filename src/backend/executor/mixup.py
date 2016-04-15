import math
price = 500
money = 10000
count_trips = 0

while (price < 700):
    stocks = round(money/price,0)
    price = round((1+stocks/690000000.0)*price,2)
    money = round(stocks*700,2)
    count_trips+=1
    print money
    print price

print count_trips
print (money)
print price