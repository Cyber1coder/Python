n = list(map(int , input("Enter numbers with space: ").split()))
print("List: ",n)
empty = [ ]
for i in range(len(n)-1,-1,-1):
    empty.append(n[i])
print("Reversed list : ",empty)