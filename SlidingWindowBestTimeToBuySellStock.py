class SlidingWindowBestTimeToBuySellStock:

    @staticmethod
    def max_profit(prices: [int]) -> int:
        l, r = 0, 1  # left - buy, right - sell
        max_p = 0

        while r < len(prices):
            # profit ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
            r += 1
        return max_p
