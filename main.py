hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#calculating the average of prices
total_prices = 0
for price in prices:
    total_prices += price
    continue
average_prices = total_prices / len(prices)
print(f'The average Haircut Price is: ${average_prices:.2f}')

#new prices, minus 5
new_prices = [x - 5 for x in prices]
print(f'New prices minus 5: ${new_prices}')

#revenue last week
total_revenue = 0
for i in range(0,len(hairstyles)):
    total_revenue+= (prices[i]*last_week[i])
    continue

print(f'Total Revenue: ${total_revenue}')

#average daily revenue
average_daily_revenue = total_revenue/7
print(f'Total daily Revenue: ${average_daily_revenue}')

#cuts under 30
cuts_under_30 = [(hairstyles[i], new_prices[i]) for i in range(0,len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)