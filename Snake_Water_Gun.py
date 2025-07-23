import random

# randomnum = random.randint(1,5)
# print(randomnum)

def game(comp,you):
    if comp==you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
    else:
        print("Invalid input")
    return

print("Computer's turn : Snake(s) Water(w) Gun(g) : ")
num = random.randint(1,3)
if num == 1:
    comp = 's'
elif num == 2:
    comp = 'w'
elif num == 3:
    comp = 'g'

you = input("Your turn : Snake(s) Water(w) Gun(g) : ")
t = game(comp,you)

print(f"Computer's choice : {comp}")
print(f"Your choice : {you}")

if t==None:
    print("Match tied!")
elif t==True:
    print("You Won!")
elif t==False:
    print("You Lose!")