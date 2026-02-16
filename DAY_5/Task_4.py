while True:
    num = int(input("Enter a number between 1 - 100 : "))

    if(num < 1):
        print("Too small")
    elif(num > 100):
        print("Too big")
    else:
        print("Valid input")
        break
