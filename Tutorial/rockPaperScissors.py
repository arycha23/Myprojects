
while (True):

    input_1 = input("Enter Rock, Paper or Scissors: ")
    input_2 = input("Enter Rock, Paper or Scissors: ")

    if(input_1.lower()=="rock" and input_2.lower()=="rock"
            or input_1.lower()=="scissors" and input_2.lower()=="scissors"
            or input_1.lower()=="paper" and input_2.lower()=="paper"):
        print("Tie")
        continue

    if(input_1.lower()=="rock" and input_2.lower()=="scissors"
        or input_2.lower()=="rock" and input_1.lower()=="scissors"):
        print("Rock wins")
        break

    elif(input_1.lower()=="rock" and input_2.lower()=="scissors"
         or input_2.lower()=="rock" and input_1.lower()=="scissors"):
        print("Scissors wins")
        break

    elif(input_1.lower()=="paper" and input_2.lower()=="rock"
         or input_2.lower()=="paper" and input_1.lower()=="rock"):
        print("Paper wins")
        break

print("Thank you for playing")
