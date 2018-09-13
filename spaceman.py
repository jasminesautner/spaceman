import random

words = ['apple', 'banana', 'pear', 'watermelon', 'peach', 'strawberry', 'kiwi', 'melon', 'starfruit']

used_letters = []

wrong_letters = []

right_letters = []

livesLeft = [7, 6, 5, 4, 3, 2, 1]

random_index = random.randint(0, 8)

# mysteryword user is trying to guess
word = words[random_index]

blanks = list("_" * len(word))

# capitalizes all potential word values to match user input
word = word.upper()

# checking letter that user has guessed 
def validate(x):
    count = 0
    for index in word:
        if index == x:
            blanks[count] = x
            blanks.append(x)
            count += 1

    # checking if letter has been previously guessed
    if x in used_letters:
        print('Already guessed letter, try again!')
        print(used_letters + '\n')

    # checking if letter is already in mysteryword
    if x in word:
        print('Correct!')
        is_right()
        right_letters.append(x)
        used_letters.append(x)
        process_input()

    # checking if letter is not in word 
    if x not in word:
        print('Oops that guess was incorrect. Please try again.')
        used_letters.append(x)
        is_wrong()
        process_input()

# recieves user input and capitalizes it, then calls validate function
def process_input():

    x = input('Enter a letter:\n')
    x = x.upper()
    print(right_letters)
    print(used_letters)
    print(blanks)
    validate(x)

# checks length of correct letters guessed with length of mysterword then prints win statement and exits game
def is_right():

    if len(right_letters) == len(word):
        print('You made it to Space!, the word was' + word + ' Thank you, play again!')
        exit()

# checks length of incorrect guesses then ends game when maximum reached
def is_wrong():
    if len(wrong_letters) >= 7:
        print('Departing back to Earth!')
        exit()

process_input()



