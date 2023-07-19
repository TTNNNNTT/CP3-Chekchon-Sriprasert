username = input("username : ")
password = input("password : ")

Mouse = 690
Keyboard = 890
Headphone = 990
Mousepad = 190
Laptop = 39990

if username == "TONNAM" and password == "212224":

    print("Welcome to IT shop")
    print(">>")
    print("Please selet your order")
    print(">>")
    print("1.Mouse  ",Mouse,"THB")
    print("2.Keyboard ",Keyboard,"THB")
    print("3.Headphone ",Headphone,"THB")
    print("4.Mousepad ",Mousepad,"THB")
    print("5.Laptop ",Laptop,"THB")

    StockITInput = int(input("Please select your number : "))

    if StockITInput == 1:
            amount = int(input("Mouse : "))
            print("price",Mouse*amount,"THB")
    elif StockITInput == 2:
            amount = int(input("Keyboard : "))
            print("price",Keyboard*amount,"THB")
    elif StockITInput == 3:
            amount = int(input("Headphone : "))
            print("price",Headphone*amount,"THB")
    elif StockITInput == 4:
            amount = int(input("Mousepad : "))
            print("price",Mousepad*amount,"THB")
    elif StockITInput == 5:
            amount = int(input("Laptop : "))
            print("price",Laptop*amount,"THB")
    else:
            print("Sorry T^T , Please select again")
    print("Thank you :D ")
else:
    print("Login Failed, Please try again")