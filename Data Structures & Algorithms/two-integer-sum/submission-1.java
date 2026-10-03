class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            Integer curr = nums[i];
            Integer temp = target - curr;

            System.out.println(temp);

            if (seen.containsKey(temp)){
                return new int[]{seen.get(temp), i};
            }

            seen.put(curr, i);
        }

        return new int[]{};
    }
}
