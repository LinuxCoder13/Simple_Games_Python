import time  
import random

level = 1
run = True
blance = 100.0
balanse_work = 0
bank_cards = ["1234-7693-2344-XXXX", "1234-5243-5423-XXXX", "1234-3232-3424-XXXX"]

while run:
    
    if blance <= 0:
        print("ты стал банкротом!")
        break

    print("-----welcome user---------")
    print("1.Show balance")
    print("2.go for a work")
    print("3.send some one money")
    print("4.Game to level up.")
    print("5.exit")
    print("---------------")
    print(f"your level is {level}")
    print("---------------")
    user = int(input("What to do (1, 2, 3, 4, 5, 6): "))
    time.sleep(1)

    if user == 1:
        print()
        print(f"your balance is ${blance:.2f}")
        print()
    elif user == 2:
        print()
        print("for 1 sec you will get $10")
        user2 = int(input("how many sec: "))
        for i in range(user2, 0, -1):
            time.sleep(1)
            print(i)
        print("work is finished")
        print()
        balanse_work = balanse_work + (user2 * 10) 
        blance = blance + balanse_work
    elif user == 3:
        user_search = input("do you want to see list (y/n): ").lower()
        if user_search == "y":
            print(bank_cards)
            user_send = int(input("Who to send money(1,2,3): "))
            if user_send == 1 or 2 or 3:
                print()
                price = float(input("how many?: "))
                while price >= blance:
                    print("you can't do that! momey is low.")
                    price = float(input("how many?: "))
                blance -= price
                print("Sending money is succes!")
                print()
            else:
                print(f"{user_send} or {price} is not valid")
        
    elif user == 5:
        print("goodbuy user!")
        break

    elif user == 4:
       while True:
        choise = input("you can lost money $20-$200 (q to quit)(s to start): ").lower()
        if choise == "q":
            break
        elif choise == "s":
            if blance >= 0:
                ran = random.randint(20, 200+1)
                blance -= ran
                level = level + 1
                print(f"you lost ${ran} but you got {level}level")
            elif blance < 0:
                break

    else:
        print(f"{user} is not valid")
        continue
