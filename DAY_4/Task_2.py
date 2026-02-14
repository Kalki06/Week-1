sum = 0
while True:
    num = int(input("Enter a number to add : "))

    if(num == 0 )  :
        print("You entered 0.")
        break

    else:
        sum += num

print(f"Your total sum is {sum}")