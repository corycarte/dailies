def two_sum(list, k):
    # Fill this in.
    seen = set()
    for i in range(len(list) - 1):
        if k - i in seen:
            return True
        seen.add(i)
    return False


print(two_sum([4,7,1,-3,2], 5))
# True
print(two_sum([8,7,1,-3,2], 5))
# True
print(two_sum([7,1,7,2], 5))
# False