import time  

run = True
blance = 100.6
balanse_work = 0
bank_cards = ["1234-7693-2344-XXXX", "1234-5243-5423-XXXX", "1234-3232-3424-XXXX"]

while run:
    
    if blance <= 0:
        print("ты стал банкротом!")
        break

    print("-----welcome user---------")
    print("1.Show balance")
    print("2.dopozit")
    print("3.go for a work")
    print("4.send some one money")
    print("5.exit")
    print("---------------")
    user = int(input("What to do (1, 2, 3, 4): "))
    time.sleep(1)

    if user == 1:
        print()
        print(f"your balance is {blance:.2f}")
        print()
    elif user == 2:
        print()
        depozit = float(input("How many put to depozin: "))
        blance += depozit
        print()
        if depozit <= 0:
            print(f"{depozit} is not valid")
            depozit = float(input("How many put to depozin (write whith float): "))
            blance += depozit
    elif user == 3:
        print()
        user2 = int(input("how many sec: "))
        for i in range(user2, 0, -1):
            time.sleep(1)
            print(i)
        print("work is finished")
        print()
        balanse_work += user2 / 1.5 
        blance = blance + balanse_work
    elif user == 4:
        user_search = input("do you want to see list (y/n): ").lower()
        if user_search == "y":
            print(bank_cards)
            user_send = int(input("Who to send money(1,2,3): "))
            if user_send == 1:
                print()
                price = float(input("how many?: "))
                blance -= price
                print("Sending money is succes!")
                print()
            elif user_send == 2:
                print()
                price = float(input("how many?: "))
                blance -= price
                print("Sending money is succes!")
                print() 
            elif user_send == 3:
                print()
                price = float(input("how many?: "))
                blance -= price
                print("Sending money is succes!")
                print()
            else:
                print(f"{user_send} or {price} is not valid")
        else:
            continue
        
    elif user == 5:
        print("goodbuy user!")
        break