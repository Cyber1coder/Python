import array
arr = array.array('i' ,[10, 20, 30, 40, 50])

arr.append(60)
print("After append:", list(arr))

arr.insert(2, 25)
print("After insert:", list(arr))

arr.remove(40)
print("After remove:", list(arr))

arr.pop()
print("After pop:", list(arr))

print("Count of 30:", arr.count(30))

arr.extend([70, 80, 90])
print("After extend:", list(arr))

arr.reverse()
print("After reverse:", list(arr))

print("Buffer info:", arr.buffer_info())

print("To bytes:", arr.tobytes())
