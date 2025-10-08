lst = [8, 3, 6, 2, 3]

lst.append(10)
lst.insert(2, 7)
lst.extend([1, 4])
lst.remove(3)
removed = lst.pop()
lst.sort()
lst.reverse()
count_3 = lst.count(3)
index_6 = lst.index(6)
length = len(lst)

print("Final list:", lst)
print("Removed element:", removed)
print("Count of 3:", count_3)
print("Index of 6:", index_6)
print("Length:", length)
