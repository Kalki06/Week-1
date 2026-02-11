marks = int(input("Enter your marks 1-100 : "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")