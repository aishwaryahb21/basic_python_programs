a =[1,0,3,0,0,4,5,0,6]
temp = []
zeros = []
for i in range(len(a)):
    if a[i] !=0:
        temp.append(a[i])
    else:
        zeros.append(a[i])
print(temp+zeros)