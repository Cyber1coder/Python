s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.add(7)
s1.update([8, 9])
s1.remove(2)
s1.discard(10)
removed = s1.pop()
union_set = s1.union(s2)
intersection_set = s1.intersection(s2)
difference_set = s1.difference(s2)
symmetric_diff = s1.symmetric_difference(s2)
is_subset = {3, 4}.issubset(s2)
is_superset = s2.issuperset({3})

print("Set 1:", s1)
print("Set 2:", s2)
print("Removed element:", removed)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_diff)
print("Is Subset:", is_subset)
print("Is Superset:", is_superset)
