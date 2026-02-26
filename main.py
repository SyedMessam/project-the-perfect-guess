import random

# Step 1: Generate a random number between 1 and 100
target = random.randint(1, 100)
guess = None
max_attempts = 3
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("You have only 3 attempts to guess the number between 1 and 100.")

# Step 2: Start the guessing loop
while attempts < max_attempts:
    try:
        guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
        attempts += 1

        if guess > target:
            print("Lower number please ❌")
        elif guess < target:
            print("Higher number please ❌")
        else:
            print(f"✅ Congratulations! You guessed the number {target} in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number!")

# Step 3: Check if user lost
if guess != target:
    print(f"\n❌ You lose! The correct number was {target}.")
