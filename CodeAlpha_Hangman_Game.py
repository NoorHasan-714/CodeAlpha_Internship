import random


def select_random_word():
    words = ["python", "hangman", "challenge", "programming", "computer", "random", "guess"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])


def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nCurrent word: {display_word(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            guessed_letters.add(guess)
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if incorrect_guesses == max_incorrect_guesses:
            print(f"Sorry, you've run out of guesses. The word was: {word}")


if __name__ == "__main__":
    hangman()
