list = [3,5,8,32,93]
max=list[0]
min = list[0]
for i in list:
    if i>max:
        max=i
    if i < min:
        min=i
    
print("Maximum = ",max)
print("Minimum = ",min)
