num = int(input("Enter a number to reverse : "))

a = num

new_num = 0
while(a > 0):
    b = a%10
    a = a//10
    new_num *= 10
    new_num += b

print(new_num)