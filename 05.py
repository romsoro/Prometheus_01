largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        snum = int(num)
    except:
        print("Invalid input")
        continue
    # print(snum)

    if largest is None:
        largest = snum
    elif snum > largest:
        largest = snum
        # print("Maximum is", largest)

    if smallest is None:
        smallest = snum
    elif snum < smallest:
        smallest = snum
        # print("Minimum is", smallest)

print("Maximum is", largest)
print("Minimum is", smallest)
