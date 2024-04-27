def armstrong():
    num=int(input("Enter a number: "))
    arms=str(num)
    result=0
    for i in arms:
        result=result+int(i)**len(arms)
    print(result)
    if result==num:
        print("armstrong")

    else:
        print("not armstrong")
armstrong()

