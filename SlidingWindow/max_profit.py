def max_profit(prices):

    
    maxProfit = 0
    
    for left in range(len(prices)):
        right = left + 1
        while right < len(prices):
            if prices[right] - prices[left] > maxProfit:
                maxProfit = prices[right] - prices[left]
            right +=1

    if maxProfit == 0:
        return 0
    else:
        return maxProfit


# max_profit([1,4,2,4,2])
# Given an array where the element at the index i 
# represents the price of a stock on day i, find the maximum 
# profit that you can gain by buying the stock once and then selling it.

