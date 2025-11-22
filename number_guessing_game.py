          # Number Guessing Game With Rating
import random

print("🙏Welcome to the number guessing game ")
print("👉i have selected a number between 1 and 100.")
print("🤖try to guess ")

# step-1: Generate random number b/w 1 and 100
secret_number = random.randint(1,100)


#step-2: initialize attempt counter 
attempts = 0

while True:
    guess = int(int(input("🎲enter your guess ")))
    attempts += 1
    if guess<1 and guess > 100:
        print("please guess a number b/w 1 and 100")
        continue

    if guess < secret_number:
        print("📈too low: try a higher number")
    
    elif guess> secret_number:
        print("📉too high: try a lower number")

    else:
        print(f"\n🎉congratulations tou guessed it in {attempts} attempts")

        # step-5: Bonus Ratting System
        if attempts <= 5:
            rating = "😎genius"
        elif attempts <= 10:
            rating = "😊average"
        else:
            rating = "😥try again"
        print(f"your rating :{rating}")
        break