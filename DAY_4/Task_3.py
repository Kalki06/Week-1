num = int(input("Enter a number to count it's digits : "))

a = num
count = 0
while(a > 0):
    a = a//10
    count += 1

print(count)