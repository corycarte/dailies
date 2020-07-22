/*
Leetcode 941 - Valid Mountain Array

Runtime => 480ms
Memory => 53.7MB
*/

class Solution {
    fun validMountainArray(A: IntArray): Boolean {
        val DOWN: Int = -1
        val NONE: Int = 0
        val UP: Int = 1
        
        val n = A.size-1
        
        var state = NONE
        
        for (i in 1..n) {
            if (state == NONE) {
                if (A[i] > A[i-1]) {
                    state = UP
                    continue
                }
            } else if (state == UP) {
                if (A[i] > A[i-1]) {
                    continue
                } else if (A[i] < A[i-1]) {
                    state = DOWN
                    continue
                }
            } else if (state == DOWN) {
                if (A[i] < A[i-1]) {
                    continue
                }
            }
            return false
        }
        
        return state == DOWN
    }

    // 252 ms example code
    fun validMountainArray_252ms(A: IntArray): Boolean {
        var n = A.size
        var i = 0

        while (i + 1 < n && A[i] < A[i + 1]) i++    // walking up hill

        if (i == 0 || i == n - 1) return false

        while (i + 1 < n && A[i] > A[i + 1]) i++    // walking down hill

        return i == n - 1   // if not the last item, then we found a mountain array        
    }
}