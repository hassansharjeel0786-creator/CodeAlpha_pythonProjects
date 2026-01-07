import random

# Predefined list of 5 words
words = ["apple", "banana", "cherry", "grape", "orange"]

# Randomly select a word
word = random.choice(words)

# Initialize game variables
guessed_letters = []
attempts_left = 6
display = ["_"] * len(word)

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 attempts to guess wrong letters.")
print("Word:", " ".join(display))

while attempts_left > 0 and "_" in display:
    # Get user input
    guess = input("Enter a letter: ").lower()

    # Check if input is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add to guessed letters
    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in word:
        print("Good guess!")
        # Update display
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        attempts_left -= 1

    # Show current state
    print("Word:", " ".join(display))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)))
    print("Attempts left:", attempts_left)

# Check win or lose
if "_" not in display:
    print("Congratulations! You guessed the word:", word)
else:
    print("Sorry, you ran out of attempts. The word was:", word)
