def findPythagoreanTriplets(nums):
    squares = set([n**2 for n in nums])

    for a in nums:
        for b in nums:
            if a**2 + b**2 in squares:
                return True
    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True