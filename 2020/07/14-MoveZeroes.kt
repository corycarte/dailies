class Solution {
    fun movezeroes(nums: IntArray): Unit {
        var k = 0

        for (x in 0..(nums.size-1)) {
            if (nums[x] != 0) {
                nums[k++] = nums[x]
            }
        }

        for (y in k..(nums.size-1)) {
            nums[y] = 0
        }
    }
}