dict = {}
while True :
    Ename = input("Enter employee's name: ")
    if Ename.lower() == "no" :
        break
    salary = int(input("Enter employee's salary: "))
    dict[Ename] = salary
    print("Information stored.")
print('Here is the dictionary: ', dict)