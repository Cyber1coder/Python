t = (10, 20, 10, 30, 40)

print("Tuple:", t)
print("Length:", len(t))
print("Count of 10:", t.count(10))
print("Index of 30:", t.index(30))
print("Minimum:", min(t))
print("Maximum:", max(t))
print("Sum:", sum(t))
print("Sorted (as list):", sorted(t))

lst = [1, 2, 3]
converted_tuple = tuple(lst)
print("Converted from list:", converted_tuple)
