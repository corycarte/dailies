def sortNums(nums):
    # Fill this in.
    listA = []
    listB = []
    listC = []
    for i in nums:
        if i == 1:
            listA.append(i)
        elif i == 2:
            listB.append(i)
        elif i == 3:
            listC.append(i)

    return(listA + listB + listC)

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]