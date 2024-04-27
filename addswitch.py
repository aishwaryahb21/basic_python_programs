a=int(input("Enter a number: "))
b=int(input("Enter b number: "))
def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)

def default():
    print("correct option")

def switch_case():
    n = int(input("Enter a function name: "))
    switch_data = {1:add,2:sub,3:mul,4:div}
    result = switch_data.get(n, default)
    result()


switch_case()
