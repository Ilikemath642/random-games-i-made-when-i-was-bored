import random
lives = 5
print("Welcome the guess a number")
max = int(input("what do you want to max amount of numbers to be: "))
number_list = [str(i) for i in range(max + 1)]
number = random.choice(number_list)
def repeat(number,lives):
    print(f'Lives left:{lives}')
    ask = input("guess a number: ")
    if ask == number:
        print("you win")
    elif lives == 1:
        print("Out of Lives")
        print(f'answer was:{number}')
    else:
        lives -= 1
        repeat(number, lives)
repeat(number, lives)
