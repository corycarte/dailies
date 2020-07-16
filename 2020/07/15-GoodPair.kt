class Solution {
    fun numIdenticalPairs(nums: IntArray): Int {
        var counter : HashMap<Int, Int> = HashMap<Int, Int>()
        
        for (num in nums) {
            if (counter.containsKey(num)) {
                var temp : Int = counter[num]!!
                counter[num] = ++temp
            } else {
                counter.put(num, 1)
            }
        }
        
        var res : Int = 0
        
        for (key in counter.keys) {
            var temp : Int = counter[key]!!
            res += ((temp * (temp - 1)) / 2)
        }
        return res
    }
}