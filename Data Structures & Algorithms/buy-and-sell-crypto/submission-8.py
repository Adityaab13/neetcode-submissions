class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        left_pointer = 0

        for right_pointer in range(1, len(prices)):
            if prices[left_pointer] > prices[right_pointer]:
                left_pointer = right_pointer
            else:
                max_p = max(max_p, prices[right_pointer] - prices[left_pointer])
        return max_p