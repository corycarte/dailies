def squareAll(nums):
    squared = []
    for i in range(0, len(nums)):
        if squared.count(nums[i]**2) < 1:
            squared.append(nums[i]**2)

    return squared

def sumSquare(nums, k):
    compliments = []

    for i in range(0, len(nums)):
        if compliments.count(nums[i]) > 0:
            return True
        else:
            compliments.append(k - nums[i])

    return False

def findPythagoreanTriplets(nums):
    squared = squareAll(nums)
    found = False
    i = 0

    while not found and i < len(squared):
        if(sumSquare(squared, squared[i])):
            found = True

        i += 1

    return found

print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
print(findPythagoreanTriplets([1, 2, 3]))
# False