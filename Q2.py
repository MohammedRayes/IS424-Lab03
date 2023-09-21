list = []
for i in range(10):
    n = int(input("Enter a Number: "))
    list.append(n)
    print("Number added to list.")
list.sort()
sortedList = list
largest = sortedList[-1]
print("The largest number is: ", largest)