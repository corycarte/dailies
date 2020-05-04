def singleNumberMap(nums):
    occurance = {}

    for n in nums:
        occurance[n] = occurance.get(n, 0) + 1

    for key, value in occurance.items():
        if value == 1:
            return key


def singleNumberXor(nums):
    unique = 0

    for n in nums:
        unique ^= n

    return unique


print(singleNumberMap([1,2,3,4,5,4,3,2,1]))
print(singleNumberMap([1,2,3,4,1,2,3,4,5]))
print(singleNumberMap([5,4,3,2,1,4,3,2,1]))

print(singleNumberXor([1,2,3,4,5,4,3,2,1]))
print(singleNumberXor([1,2,3,4,1,2,3,4,5]))
print(singleNumberXor([5,4,3,2,1,4,3,2,1]))
