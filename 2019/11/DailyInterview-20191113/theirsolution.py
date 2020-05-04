def distance(s1, s2):
  if len(s1) == 0 or len(s2) == 0:
    return max(len(s1), len(s2))

  return min(distance(s1[1:], s2) + 1,
         distance(s1, s2[1:]) + 1,
         distance(s1[1:], s2[1:]) if s1[0] == s2[0]
         else distance(s1[1:], s2[1:]) + 1)
         
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
