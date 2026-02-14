# Broken infinite loop
# count = 1

# while count <= 5:
#     print("Count is:", count)

# why this loop is printing infinitly ?
# In this loop the count is not increase after completing the task and the loop condition is count <= 5
# so if count will not change and the consition will never meet and loop will print countinuosly for infinte times.

# Correct loop

count = 1

while count <= 5:
    print("Count is:", count)
    count += 1