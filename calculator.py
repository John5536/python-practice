def print_menu():
    print("====================")
    print("1)sum")
    print("2)substract")
    print("3)multiply")
    print("4)divide")

print_menu()
option = input("select the option").lower


num1 =float(input("PLease provide a number"))
num2 = float(input("please providea second number"))

if option == "1":
    total = num1 + num2
    print("the total is:" +  str(total))
elif option == "2":
    total = num1 - num2
    print("the total is:" +  str(total))
elif option == "3":
    total = num1 * num2
    print("the total is:" +  str(total))
elif option == "4":
    if num2 == 0:
        print("you're trying to devide by zero")
    else:
        total = num1 / num2
        print("the total is:" +  str(total))
    

