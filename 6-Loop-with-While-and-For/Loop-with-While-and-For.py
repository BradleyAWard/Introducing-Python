# Code 1
# A simple while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# Code 2
# Break out of a while loop
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 5:
        break

# Code 3
# Skip iterations with continue
count = 1
while count <= 10:
    print(count)
    count += 1
    if count == 5:
        count += 2
        continue

# Code 4
# Using range()
for x in range(2, 10, 2):
    print(x)