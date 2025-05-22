import random
secret_number=random.randint(1,10)
guess=0
while guess!=secret_number:
    guess=int(input("Guess number between 1 and 10"))
    if guess < secret_number:
        print("Tool low")
    elif guess > secret_number:
     print("Too high")

    print ("Congratulation ! You guessed it right")

