import os
import random
k=0
while k<10:
    print(" ")
    print(" ")
    print("...................................................../\/\/\/\/\/\/\/\..................................................... ")
    print(" ")
    print(" ")
    print("                                                  Name & Gali Generator ")
    print("                                                      -  -  -  -  -        ")
    print(" ")
    print(" ")
    number = int(input("How Many Names Do You Want?:"))
    print(" ")
    print(" ")
    number2 = 100/number
    name = ["Kumud","Vishal","Meghna","Saran","Dholu","Majnu","Nobita", "John","Baba Ram Dev", "Shaktiman"," Chotha Bheem","Babita Ji","Madhuri","Tarak Meheta","Mahesh", "Deepak", "Raja", "Kavya", "Mr.White", "Stuart Little", "Sanjana", "Pakistan","Champak Chacha","Manohar","Vishal","Mogli","Dumbledore","Phineas and Ferb","Person Reading this is","Kabir","Gabbar","King Louis the IV","King Louis the III","Glenn Quagmire","Ram Aur Lakkhan","Karan Arjun"]
    gali = ["Gay","MILF","Dick Head","lodu","Gandu","Rand", "Horny","HIV+ ","BDSM","pedofile","Lodu Chand","Chirand", "eats shit","Pervert","Little Bitch","Daily Wage Labour","Nigga","Cunt","Macchar ki Jhaant","Middle Class","the Rapist","Bitch","Gaddhe ki gand","Child Molester","is mentally challanged","is a pain in the ass","Virgin","Dalal","is full of shit"]
    me = ["God","Legend","is epic","Horny","the best"]

    print(" ")
    print("  -.-:-.-:-.-:-.-:-.-:-.- ",round(number),"Random Names are Listed Below")
    print(" ")
    i = 0
    while i < 100:
        a = random.choice(name)
        b = random.choice(gali)
        c = random.choice(me)
        if a == "Kumud":
            print("                                  .......    ",a, c)
            print(" ")
        else:    
            print(" ")
            print("                                  .......    ",a, b)
            print(" ")
            print(" ")
        i = i+number2
    print("                                                                                         Name and Gali Count :", number)
    k=1
