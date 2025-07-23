import random

def toss():
    return random.randint(1,2)

def bowl():
        return random.randint(1,6)
    

def bat():
    return random.randint(1,6) 
     

bowlnum = bowl()
batnum = bat()
num = toss()

if num==1:
    print("CPU won the toss!")
    a = False
else:
    print("You won the toss!")
    a = True

if a == True:
    a1 = input("Choose either Bat(b) or Bowl(f) : ")
    if a1 == 'b':
        print("You chose to Bat")
        bowl()
        bat = 0
        batsum = 0
        while(bowlnum!=bat):
            bat = int(input("Enter batting number : "))
            if(bowl()==bat):
                print("CPU bowling number :",bowl())
                print("OUT!")
                print("Batting total score :",batsum)
            else:
                print("CPU bowling number :",bowl())
                batsum = batsum + bat
                print("Batsum =",batsum)
            
    elif a1 == 'f':
        print("You chose to Bowl")
        bat()
        bowl = 0
        batsum = 0
        while(bat()!=bowl):
            bowl = int(input("Enter bowling number : "))
            if(bat()==bowl):
                print("CPU batting number :",bat())
                print("OUT!")
                print("Batting total score :",batsum)
            else:
                print("CPU batting number :",bat())
                batsum = batsum + bat()
                print("Batsum =",batsum)
                
    else:
        print("Invalid choice")

elif a == False:
    a2 = toss()
    if a2==1:
        a2='b'
    else:
        a2='f'
    print(f"Choose either Bat(b) or Bowl(f) : {a2}")
    if a2 == 'b':
        print("CPU chose to bat")
        bat()
        bowl = 0
        batsum = 0
        
        while(bat()!=bowl):
            bowl = int(input("Enter bowling number : "))
            if(batnum==bowl):
                print("CPU batting number :",bat())
                print("OUT!")
                print("Batting total score :",batsum)
            else:
                print("CPU batting number :",bat())
                batsum = batsum + bat()
                print("Batsum =",batsum)
    else:
        print("CPU chose to bowl")
        bowl()
        bat = 0
        batsum = 0
        
        while(bowl()!=bat):
            bat = int(input("Enter batting number : "))
            if(bowl()==bat):
                print("CPU bowling number :",bowl())
                print("OUT!")
                print("Batting total score :",batsum)
            else:
                print("CPU bowling number :",bowl())
                batsum = batsum + bat
                print("Batsum =",batsum)

else:
    print("Choose valid choice")

