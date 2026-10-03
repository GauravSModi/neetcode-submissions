class Solution {
    public int longestConsecutive(int[] nums) {
        // Find starting of sequences
        // Build sequences
        // Keep track of longest

        int longest = 0;
        HashMap<Integer, Integer> mp = new HashMap();

        for (int i = 0; i < nums.length; i ++) {
            mp.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i ++) {
            if (mp.get(nums[i]-1) != null) {
                continue;
            }

            int currNum = nums[i];
            int seqLen = 1;
            // Current number is a starting point for a potential sequence
            // Create and keep track of sequence
            
            while (mp.get(currNum + 1) != null){
                seqLen += 1;
                currNum += 1;
            }

            if (seqLen > longest) {
                longest = seqLen;
            }
        }

        return longest;
    }
}
