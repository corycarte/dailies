class Solution {
    public int trap(int[] height) {
        int n = height.length;
        
        if (n < 1)
            return 0;
        
        // Step 1: find max to left of index
        int[] max_left = new int[n];
        
        int currMax = 0;
        for (int i = 0; i < n; ++i) {
            currMax = Math.max(currMax, height[i]);
            max_left[i] = currMax;
        }
        
        // Step 2: find max to right of index
        int[] max_right = new int[n];
        
        currMax = 0;
        for (int i = n-1; i > -1; --i) {
            currMax = Math.max(currMax, height[i]);
            max_right[i] = currMax;
        }
        
        // Step 3: compute water trapped at index
        // Step 4: sum trapped water
        int total = 0;
        
        for (int i = 0; i < n; ++i) {
            total += Math.min(max_left[i], max_right[i]) - height[i];
        }
        
        
        return total;
    }
}