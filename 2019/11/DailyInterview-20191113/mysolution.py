def distance(s1, s2): # Fill this in.
    if(s1 == s2):
        return 0

    longer = max(len(s1), len(s2))
    stop = min(len(s1), len(s2))
    dist = 0

    i = j = 0

    while(i < stop and j < stop):
        if s1[i] != s2[j]:
            #insertion
            if j + 1 < stop and s1[i] == s2[j + 1]:
                dist += 1
                j += 1
            #deletion
            elif i + 1 < stop and s1[i + 1] == s2[i]:
                dist += 1
                i += 1
            #modification
            else:
                dist += 1
        i += 1
        j += 1

    while i < longer and j < longer:
        dist += 1
        i += 1
        j += 1

    return dist

print(distance('ate', 'hate'))
# 1 - insertion
print(distance('hate', 'ate'))
# 1 - deletion
print(distance('kate', 'hate'))
# 1 - modification
print(distance('hate', 'hated'))
# 1 - insertion
print(distance('hated', 'hate'))
# 1 - deletion
print(distance('hate', 'hate'))
# 0

