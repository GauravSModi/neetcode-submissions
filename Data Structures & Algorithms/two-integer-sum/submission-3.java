class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i ++) {
            int desired = target - nums[i];

            if (seen.containsKey(desired)) {
                return new int[] {seen.get(desired), i}; 
            }

            seen.put(nums[i], i);
        }

        return new int[] {};
    }
}
