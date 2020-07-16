class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; ++i) {
            if (counter.containsKey(nums[i])) {
                int temp = counter.get(nums[i]);
                counter.put(nums[i], (temp + 1));
            } else {
                counter.put(nums[i], 1);
            }
        }
        
        int res = 0;
        
        for (int j : counter.keySet()) {
            int temp = counter.get(j);
            res += ((temp * (temp - 1)) / 2);
        }
        
        return res;
    }
}