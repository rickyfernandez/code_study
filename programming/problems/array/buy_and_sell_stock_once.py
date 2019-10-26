from typing import List

def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_so_far, max_so_far = prices[0], 0
    for i in range(len(prices)):
        profit = prices[i] - min_so_far
        min_so_far = min(min_so_far, prices[i])
        max_so_far = max(max_so_far, profit)
    return max_so_far

if __name__ == "__main__":
    x = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    print(buy_and_sell_stock_once(x))
