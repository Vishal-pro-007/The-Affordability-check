car1 = 10000
car2 = 20000
car3 = 40000

while True:
    try:
        budget = int(input("Enter your budget or type 0 for exit: "))
        if budget == 0:
            print("Next time!")
            break
        if budget == car1:
            print("You can Afford car1!")
        elif budget == car2:
                print("You can Afford car2 and car1!")
        elif budget == car3:
                    print("You can afford car 3 and car 1!")
        elif budget < car2:
                        print("Work harder to afford car2!")
        elif budget < car3:
                            print("Work harder to afford car3!")
        elif budget <= car1:
                                print("Youre financially strained")
        elif budget > car3:
            print("Youre rich enough to be able to buy all the cars!")
    except ValueError:
        Print("Invalid")
