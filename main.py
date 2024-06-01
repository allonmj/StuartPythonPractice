import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'computer', 'science', 'keyboard'  'stuart', 'commit', 'implementation',  'Configure',  'marathon,']
    return random.choice(words)

def display_hangman(tries):
    stages = ["""
                 -----
                 |   |
                 O   |
                /|\\  |
                / \\  |
                     |
                --------
                """,
                """
                 -----
                 |   |
                 O   |
                /|\\  |
                /    |
                     |
                --------
                """,
                """
                 -----
                 |   |
                 O   |
                /|\\  |
                     |
                     |
                --------
                """,
                """
                 -----
                 |   |
                 O   |
                /|   |
                     |
                     |
                --------
                """,
                """
                 -----
                 |   |
                 O   |
                 |   |
                     |
                     |
                --------
                """,
                """
                 -----
                 |   |
                 O   |
                     |
                     |
                     |
                --------
                """,
                """
                 -----
                 |   |
                     |
                     |
                     |
                     |
                --------
                """
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6
    print("Welcome to Hangman!")
    
    while tries > 0 and len(word_letters) > 0:
        print(display_hangman(tries))
        print(f"You have {tries} tries left.")
        print("Guessed letters:", ' '.join(guessed_letters))
        
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word:", ' '.join(word_display))
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"Letter {guess} is not in the word.")
        
    if tries == 0:
        print(display_hangman(tries))
        print(f"You lost! The word was '{word}'.")
    else:
        print(f"Congratulations! You guessed the word '{word}'.")

if __name__ == "__main__":
    hangman()

