import random
import word_list
import HangMan_idol

# Choose a random word from the fruits list
chosen_word = random.choice(word_list.fruits)
lives = 6

# Initialize the display with underscores
display = ['_' for _ in range(len(chosen_word))]

print("Initial Display: ", display)
print("Length of Display: ", len(display))
print(f"Hint: It is a Fruit Name\nAnd the first letter is '{chosen_word[0]}' and the last letter is '{chosen_word[-1]}'")

game_over = False

while not game_over:
    guessed_letter = input("Guess a Letter: ").lower()

    # Check if guessed_letter is in the chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print("Current Display: ", display)

    # Reduce lives if the guessed letter is not in the word
    if guessed_letter not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print(f"Sorry, you lost the game! The word was '{chosen_word}'.")

    # Check if the player has guessed the word
    if '_' not in display:
        game_over = True
        print("Congratulations, you won the game!")

    # Print the current hangman idol
    print(HangMan_idol.idols[lives])
