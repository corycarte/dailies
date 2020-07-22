class Solution {
    // Runtime 328 ms -> Faster than 20% of Kotlin solutions
    // Memory  35.5MB -> Less than 40% of Kotlin solutions
    fun getMax(a: Int, b: Int): Int {
        if (a > b) {
            return a
        } else {
            return b
        }
    }
    
    fun getMin(a: Int, b: Int): Int {
        if (a > b) {
            return b
        } else {
            return a
        }
    }
    
    fun trap(height: IntArray): Int {
        var n = height.size-1
        
        // Step 1: find max to left of index
        var max_left = IntArray(n+1)
        var currMax = 0
        for (i in 0..n) {
            currMax = getMax(currMax, height[i])
            max_left[i] = currMax
        }
        
        // Step 2: find max to right of index
        var max_right = IntArray(n+1)
        currMax = 0
        for (i in n downTo 0) {
            currMax = getMax(currMax, height[i])
            max_right[i] = currMax
        }
        
        // Step 3: compute water trapped at index
        // Step 4: sum trapped water
        var res = 0
        
        for (i in 0..n) {
            res += ((getMin(max_left[i], max_right[i])) - height[i]);
        }        
        
        return res
    }
}