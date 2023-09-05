# match case in python. it acts like switch case

a = int(input("Please enter a number: "))

match a:
    case 1:
        print("you are in case 1")
    case 2:
        print("you are in case 2")

    case _ if a != 90:
        print(a, "not equal 90")

    case _ if a != 80:
        print(a, "not equal 80")
    case _:
        print("you are in default case")
