username=['aishu','radhu','teju']
userpassword=['1234','5678','9012']
name=input('Enter your name: ')
for a,b in enumerate(username):
    if b==name:
        password=input('Enter your password: ')
        if password==userpassword[a]:
            print("welcome")




