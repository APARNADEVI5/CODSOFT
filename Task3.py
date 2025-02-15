import random
def genpass(len):
    char= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    passw= ""
    for i in range(len):
        passw+= random.choice(char)
    return passw
len = int(input("Enter the length of the password: "))
passw= genpass(len)
print("the generated password is:", passw)


