answer = input ("what you like to play? (yes/no) ")
if answer.lower().strip() == "yes":
    answer = input("you reach a crossroads, would you like to left or right?").lower().strip()
    if answer == " left ":
        answer = input("you encounter a monster, would you like to run or attack.")
        if answer == "attack":
            print("this was not the greatest idea,you lost!")
        else:
            print ("Good choice, you made it away safely.")
            answer = input ("you see a car and a plane. which would you like to choose? (car/plane)")
            if answer== "plane":
                print("Unfortunatly you fly but your plane crashed sorry!  .. Game Over  ")
            else: 
                print(" you won !")
    elif answer == "right":
        print("you walk aimlessly to the right and fall on a  patch of ice . you injure your leg and cannot continue. Game over! ")
    else:
        print("Invalid choice, you lost!")
else:
    print("that's too bad !")            
