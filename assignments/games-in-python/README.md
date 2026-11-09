
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game that uses random selection, strings, loops, conditionals, and user input to help a player guess a hidden word.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Prepare the word and game state before starting a round.

#### Requirements
Completed program should:

- Randomly select one secret word from the provided `words` list.
- Initialize a collection to track guessed letters and a counter for incorrect guesses.
- Set a maximum number of incorrect guesses.

### 🛠️ Run a Hangman Round

#### Description
Implement the game loop so the player can guess letters until they reveal the secret word or run out of attempts.

#### Requirements
Completed program should:

- Show the secret word as hidden letters, updating the display when a guessed letter appears in the word.
- Ask the player for a letter and update the game state for correct and incorrect guesses.
- Show how many incorrect guesses remain after each guess.
- End the round when the word is revealed or the maximum number of incorrect guesses is reached.
- Display a win message when the player reveals the word, or a loss message and the secret word when attempts run out.
