print("Welcome to word game ")
import pyttsx3
import time
import random
import enchant  # Module for spell checking
import os

engine = pyttsx3.init()
engine.say("Hello Children! I am Ellaalan! Let us Play interesting   word game!")
engine.runAndWait()

def check_spelling(word):
    d = enchant.Dict("en_US")  # Using the English US dictionary
    return d.check(word)

engine.say("Enter your good  name:")
engine.runAndWait()
name = input()
a = name[0]

engine.say("To start the game, first type a word that starts with the initial letter of your name.")
engine.runAndWait()
engine.say("The next word you type should start with the letter suggested by the previous word.")
engine.runAndWait()
engine.say("Do not use spaces in your word. The game will end if you do.")
engine.runAndWait()
engine.say("Each word can only be used once.")
engine.runAndWait()

score = 0
word_list = []
used_words = set()

# Pause for 1 second
time.sleep(1)

engine.say("How many words do you want to play?")
engine.runAndWait()
num = int(input())

# Game loop
for i in range(num):
    engine.say("Enter the word:")
    engine.runAndWait()
    word = input().strip().lower()  # Remove leading/trailing spaces and convert to lowercase

    if word[0] == a and " " not in word and word not in used_words:
        if check_spelling(word):
            if i == 0:
                engine.say(f"Congratulations {name}! You earned 5 points for your first word.")
                engine.runAndWait()
                score += 5
            else:
                engine.say(f"Congratulations {name}! That word is spelled correctly.")
                engine.runAndWait()
                score += 5

            x = random.randint(0, len(word) - 1)
            suggestion = word[x]
            engine.say(f"Your word is: {word}, and your suggested letter is: {suggestion}.")
            engine.runAndWait()
            a = suggestion
            word_list.append(f"{word}, suggested letter is: {suggestion}")
            used_words.add(word)
        else:
            engine.say(f"Sorry {name}, '{word}' is misspelled. Please try again.")
            engine.runAndWait()
            i -= 1  # Retry the same iteration

    else:
        engine.say(f"Game over, {name}. You did not follow the rules. Final score is {score}.")
        engine.runAndWait()
        break

# Final score message
engine.say(f"Thank you {name}, your final score is {score}.")
engine.runAndWait()

# Save game details to file in the user's documents folder
document_folder = os.path.join(os.path.expanduser('~'), 'Documents')
file_path = os.path.join(document_folder, 'game.txt')

with open(file_path, "w") as f:
    f.write(f"Hello {name}, your score is: {score}.\n")
    f.write("Your words and their suggestions are listed below:\n")
    for item in word_list:
        f.write(item + "\n")

engine.say(f"Your game details have been saved in a file called game.txt in your Documents folder.")
engine.runAndWait()

# Pause for 8 seconds
time.sleep(8)

print(" Thank you play this  word game By: S. Prethepan")