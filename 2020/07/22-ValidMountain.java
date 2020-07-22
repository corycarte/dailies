/*
Leetcode 941 - Valid Mountain Array

Runtime => 1ms
Memory => 40.4MB
*/

class Solution {
    public boolean validMountainArray(int[] A) {
        int DOWN = -1;
        int NONE = 0;
        int UP = 1;
        
        
        int state = NONE;
        
        for (int i = 1; i < A.length; ++i) {
            if (state == DOWN) {
                if (A[i] < A[i-1]) {
                    continue;
                }
            } else if (state == NONE) {
                if (A[i]> A[i-1]) {
                    state = UP;
                    continue;
                }
            } else if (state == UP) {
                if (A[i] > A[i-1]) {
                    continue;
                } else if (A[i] < A[i-1]) {
                    state = DOWN;
                    continue;
                }
            }
            
            return false;
        }
        
        return state == DOWN;
    }
}