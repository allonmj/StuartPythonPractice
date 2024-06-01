def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'computer', 'science', 'keyboard', 'stuart', 'commit', 'implementation',  'Configure']
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

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
