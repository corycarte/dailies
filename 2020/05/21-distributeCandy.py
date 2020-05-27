def distributeCandies(self, candies, num_people):
    """
    runtime : O(n) 32ms on leetcode
    runspace: O(n) 12.6 MB on leetcode
    :type candies: int
    :type num_people: int
    :rtype: List[int]
    """
    res = [0 for i in range(num_people)]
    numCandy = 1
    dist = 0
    
    while candies > 0:
        if numCandy < candies:
            res[dist] += numCandy
            candies -= numCandy
        else:
            res[dist] += candies
            candies -= candies
            
        numCandy += 1
        
        if dist + 1 < num_people:
            dist += 1
        else:
            dist = 0
            
    return res
            