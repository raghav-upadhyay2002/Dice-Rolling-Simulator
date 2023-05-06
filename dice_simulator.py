import random
while True:
    print("What you want")
    user = int(input("1.Roll dice      2.Exit\n"))
    if user == 1:
        print("Number is: ")
        print(random.randint(1, 6))
    elif user == 2:
        break
    else:
        print("Wrong Input")
        break
