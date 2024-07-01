prices = [7,1,5,3,6,4]

purchase = prices[0]
max_profit = 0
n = len(prices)

for i in range(1,n):
    cost = prices[i] - purchase
    max_profit = max(max_profit, cost)
    purchase = min(purchase, prices[i])

print(f"MAX: {max_profit}")