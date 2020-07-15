class Solution {
    public void moveZeroes(int[] nums) {
        int arrSize = nums.length;
        
        int k = 0;
        
        for(int i = 0; i < arrSize; ++i) {
            if (nums[i] != 0)
                nums[k++] = nums[i];
        }
        
        for (int j = k; j < arrSize; ++j) {
            nums[j] = 0;
        }
    }
}