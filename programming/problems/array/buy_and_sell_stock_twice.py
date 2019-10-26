from typing import List

def buy_and_sell_stock_twice(prices: List[float]) -> float:
    first_buy_sell = [0]*len(prices)
    min_price_so_far, max_profit = prices[0], 0

    for i in range(len(prices)):
        min_price_so_far = min(min_price_so_far, prices[i])
        max_profit = max(max_profit, prices[i] - min_price_so_far)
        first_buy_sell[i] = max_profit

    max_price_so_far, max_profit = prices[-1], 0
    total = 0
    for i in reversed(range(len(prices))):
        max_price_so_far = max(max_price_so_far, prices[i])
        max_profit = max(max_profit, max_price_so_far - prices[i])
        total = max(total, max_profit + first_buy_sell[i])
    return total

if __name__ == "__main__":
    #x = [12, 11, 13, 9, 12, 8, 14, 13, 15]
    x = [1, 5, 3, 7, 12]
    print(buy_and_sell_stock_twice(x))
