class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int profit = 0;

        if (prices.length == 1) {
            return profit;
        }

        while (r < prices.length) {
            if (prices[l] > prices[r]) {
                l = r;
            } else {
                int newProfit = prices[r] - prices[l];
                profit = (profit < newProfit) ? newProfit : profit;
            }
            r = r+1;
        }

        return profit;
    }
}
