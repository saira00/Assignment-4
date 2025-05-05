import random

def choose_word():
    words = ["python", "hangman", "developer", "streamlit", "project", "challenge"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     /|\
           |     / \\
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\
           |     /
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]
    return stages[tries]

def play_hangman():
    while True:
        word = choose_word()
        word_letters = set(word)
        guessed_letters = set()
        tries = 6
        
        print("Welcome to Hangman!")
        while tries > 0 and word_letters:
            print(display_hangman(tries))
            print("Word: ", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
            print("Guessed letters:", " ".join(guessed_letters))
            
            guess = input("Enter a letter: ").lower()
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word_letters:
                guessed_letters.add(guess)
                word_letters.discard(guess)  # Use discard to avoid errors
                print("Good guess!")
            else:
                guessed_letters.add(guess)
                tries -= 1
                print("Wrong guess!")
        
        print(display_hangman(tries))
        if not word_letters:  # Check if all letters are guessed
            print("Congrats! 🎉 You guessed the word correctly:", word)
        else:
            print("Game Over! The word was:", word)
        
        # Play Again Option
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_hangman()
