import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

logo = hangman_art.logo
print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"already guessed this letter '{guess}', try another letter")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:

        print(f"this letter {guess} is not in the word , you loss a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"the word is {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    if lives < 0:
        end_of_game = True
        print("you loss")
        print(f"the word is {chosen_word}")

    stages = hangman_art.stages
    print(stages[lives])