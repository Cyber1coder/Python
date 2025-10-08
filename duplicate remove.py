num=list(map(int,input("Enter numbers: ").split()))
empty = [ ]
for i in num:
    if i not in empty:
        empty.append(i)

print("Without duplicates: ",empty)
