# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
# return 0.

def maxProfit(prices):
    buy = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] <buy:
            buy = prices[i]
        elif prices[i] - buy >max_profit:
            max_profit = prices[i] - buy
    return max_profit

#example usage
prices = [7,1,5,3,6,4]
print(maxProfit(prices))  # Output: 5