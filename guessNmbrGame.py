import random
secret = random.randint(1, 99)

while True:
    numGame = int(input("Enter a number: "))

    if numGame == secret:
        print("Congraulation You correct")
        break
    elif numGame>secret:
        print("To high number")
    else:
        print("To low number")
