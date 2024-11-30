import random

def guess_game(lives, number):
    cheat_code = "wwssadadba"
    while lives > 0:
        print(f'Lives left: {lives}')
        ask = input("Guess a number: ").strip()
        if ask == cheat_code:
            print(f"Cheat code activated! The correct number is: {number}")
            continue
        if ask == number:
            print("You win!")
            return
        else:
            lives -= 1
            if lives == 0:
                print("Out of lives!")
                print(f'The correct answer was: {number}')
            else:
                print("Wrong guess. Try again.")

def main():
    print("Welcome to the Guess a Number Game!")
    lives = 5
    mode = input("Choose mode: own number or random (o/r): ").strip().lower()
    
    if mode == "r":
        max_value = int(input("What should the maximum number be? "))
        number = str(random.randint(0, max_value))
        guess_game(lives, number)
    elif mode == "o":
        number = input("Enter your number: ").strip()
        print("\nTell the guesser to start guessing!")
        guess_game(lives, number)
    else:
        print("Invalid mode selected. Please restart the game.")

main()