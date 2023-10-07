play = True

while play:
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    question = input("Do you want to add, subtract, multiply, or divide your number? (A/S/M/D)")

    if question == "A":
        print(int(num1) + int(num2))
    if question == "S":
        print(int(num1) - int(num2))
    if question == "M":
        print(int(num1) * int(num2))
    if question == "D":
        print(int(num1) / int(num2))

    play_again = input("Do you want to play again? (Y/N)")
    if play_again == "N":
        play = False
        break
    if play_again == "Y":
        play = True
