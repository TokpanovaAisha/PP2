
import random 

def GuessNumber():    
    
    number = random.randint(1, 20)
    name = input("Hello, what is your name? ")
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    cnt = 0
        
    while True:
        attempt = int(input("Take a guess: "))
        cnt += 1
        
        if attempt > number:
            print("Your guess is too high.")
        elif attempt < number:
            print("Your guess is too low.")
        else:
            print(f'Good job, {name}! You guessed my number in {cnt} guesses!')
            break
        
GuessNumber()