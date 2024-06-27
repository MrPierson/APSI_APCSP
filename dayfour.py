import requests
import random
import textwrap

url = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
response = requests.get(url)
word_list = response.text.split()

def display_word(word, target):
    display = []
    for i in range(len(word)):
        if word[i] == target[i]:
            display.append(word[i])
        elif word[i] in target:
            display.append(f"[{word[i]}]")
        else:
            display.append("[ ]")
    return " ".join(display)

def wordle(attempts = 6):
    target_word = random.choice(word_list).upper()
    word_length = len(target_word)
    print(
    textwrap.dedent(f"""
    Guess the {word_length}-letter word
    1. If a letter is in the correct spot, it will appear without brackets.
    2. If a letter is in the word but the incorrect spot, it will appear with brackets.
    3. If a letter is not in the word, the brackets will be empty.
    4. Enter "quit" or "exit" to stop playing.
    """
    ))
    print("[ ] " * word_length)
    for attempt in range(attempts):
        guess = input("Enter a word: ").upper()
        if guess in ["QUIT", "EXIT"]:
            print("Adios!")
            break
        elif len(guess) != word_length:
            print(f"Please enter a {word_length}-letter word.")
            continue
        
        if guess == target_word:
            print(f"Congratulations! You guessed the word: {target_word}")
            break
        
        print(display_word(guess, target_word))
        
        if attempt == attempts - 1:
            print(f"Game over! You've used all your attempts. The word was: {target_word}")

if __name__ == "__main__":
    wordle()
