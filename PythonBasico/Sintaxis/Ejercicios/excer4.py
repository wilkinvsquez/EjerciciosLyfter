count = 1
temp = 0
while count <= 3:
    number = int(input(f"Please enter number: "))
    if number > temp:
        temp = number
    count += 1
print(f"The largest number entered was: {temp}")