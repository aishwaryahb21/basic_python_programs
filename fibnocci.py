n=int(input("Enter a number:"))
a=0
b=1
s=0
for x in range(n):
    print(s)
    s=a+b
    b=a
    a=s