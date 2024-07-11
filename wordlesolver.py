from collections import Counter
import random
#COMET, BRINK, FLASH, PUDGY
# This word will be altered to the word trying to solve for the day.
currentword = "doubt"
j = 0
x = 0
counter = 0
arraysize = 0
# Words hard coded for success rate.
guess1 = "comet"
guess2 = "flash"
guess3 = "brink"
guess4 = "pudgy"
guesses = ["comet", "flash", "brink", "pudgy"]

letter0 = []
letter1 = []
letter2 = []
letter3 = []
letter4 = []

# Empty array of ALL 5 letter words.
fiveletterwords = [] 
# Five letter words after computation of Wordle
fiveletteraccurate = []
# Guess array
guesscharacter = []
currentcharacter = []
containscharacter = []
updatedarray = []
invalidchar = []
filtered_words = []
refined_list = []
tester = []
# Uses a score based system to find best word.
bestword = ""
scored_words = ["meow"]
wordlist = []
gameover = 0

# Final Array
final = ["", "", "", "", ""]
# Memory storage of each guess
memory1 = ["", "", "", "", ""]
memory2 = ["", "", "", "", ""]
memory3 = ["", "", "", "", ""]
memory4 = ["", "", "", "", ""]
memory5 = ["", "", "", "", ""]
memory6 = ["", "", "", "", ""]

def openfile():
    # Store all dictionary words inside this array.
    # All potential wordle 5 letter words.
    with open("/YOUR_DIRECTORY_HERE", "r") as wordlist:
        for line in wordlist:
            fiveletterwords.append(line.rstrip('\n'))

# This function concats the letters that are "found in the guess" to one word.
def catguess():
    global catresult
    catresult = ''.join(containscharacter)
    catresultlen = len(catresult)
    catresult_counter = Counter(catresult)
    if (catresultlen == 5):
        for word in fiveletterwords:
            word_counter = Counter(word)
            if all(word_counter[char] <= catresult_counter[char] for char in word_counter) and all(char in catresult for char in word):
                if all(char not in invalidchar for char in word):
                    fiveletteraccurate.append(word)
    # If we dont have all 5 letters.
    else:
        for word in fiveletterwords:
            if all(char in word for char in catresult):
                if all(char not in invalidchar for char in word):
                    fiveletteraccurate.append(word)

def filteredsix():
    global filtered_words
    for word in fiveletteraccurate:
        match = True
        for i, char in enumerate(memory6):
            if char and word[i] != char:
                match = False
                break
        if match:
            filtered_words.append(word)
    return filtered_words

# This function checks the guesses we have made, against the results of those guesses. It checks if a specific letter is invalid in the column. 
# Allows us to finetune our guesses
def columns():
    for word in guesses:
        if word[0] != currentword[0]:
            letter0.append(word[0])
        if word[1] != currentword[1]:
            letter1.append(word[1])
        if word[2] != currentword[2]:
            letter2.append(word[2])
        if word[3] != currentword[3]:
            letter3.append(word[3])
        if word[4] != currentword[4]:
            letter4.append(word[4])

# Used to remove unnecessary words.
def finetunearray(fiveletteraccurate):
    for word in fiveletteraccurate:
        remove_word = False
        if word[0] in letter0:
            remove_word = True
        elif word[1] in letter1:
            remove_word = True
        elif word[2] in letter2:
            remove_word = True
        elif word[3] in letter3:
            remove_word = True
        elif word[4] in letter4:
            remove_word = True
        
        if not remove_word:
            refined_list.append(word)

    return refined_list
                    
# Can further implement this when no actual word is given. 
# Currently all guess functions implemented for GREEN only.
def firstguess():
    for value in guess1:
        # Appends hardcoded guess value into an array.
        guesscharacter.append(value)
    for char in currentword:
        # Append the solution word to an array.
        currentcharacter.append(char)
    # Iterates through characters, if exact matching (green) store to array.
    for i in range(5):
        if guesscharacter[i] == currentcharacter[i]:
            memory1[i] = guesscharacter[i]
        elif guesscharacter[i] == '': 
            memory1[i] = ''
    # Check if a letter is found inside a word.
    for i in range(5):
        for j in range(5):
            if guesscharacter[i] == currentcharacter[j]:
                containscharacter.append(guesscharacter[i])
        for guess_char in guess1:
            if guess_char not in currentword:
                invalidchar.append(guess_char)
    
def secondguess():
    guesscharacter = []
    for value in guess2:
        guesscharacter.append(value)
    for i in range(5):
        if ((guesscharacter[i] == currentcharacter[i]) & (memory2[i] == '')) :
            memory2[i] = guesscharacter[i]
        elif guesscharacter[i] == '': 
            memory2[i] = ''
    # Check if a letter is found inside a word.
    for i in range(5):
        for j in range(5):
            if guesscharacter[i] == currentcharacter[j]:
                containscharacter.append(guesscharacter[i])
        for guess_char in guess2:
            if guess_char not in currentword:
                invalidchar.append(guess_char)

def thirdguess():
    global fiveletteraccurate, gameover
    catguess()
    lenguess = len(fiveletteraccurate)
    if lenguess == 1:
        print("Final guess is:", fiveletteraccurate[0])
        gameover = 1
        return gameover
    fiveletteraccurate = []
    guesscharacter = []
    for value in guess3:
        guesscharacter.append(value)
    for i in range(5):
        if ((guesscharacter[i] == currentcharacter[i]) & (memory3[i] == '')) :
            memory3[i] = guesscharacter[i]
        elif guesscharacter[i] == '': 
            memory3[i] = ''
    # Check if a letter is found inside a word.
    for i in range(5):
        for j in range(5):
            if guesscharacter[i] == currentcharacter[j]:
                containscharacter.append(guesscharacter[i])
        for guess_char in guess3:
            if guess_char not in currentword:
                invalidchar.append(guess_char)

def fourthguess():
    global gameover, fiveletteraccurate
    catguess()
    lenguess = len(fiveletteraccurate)
    if lenguess == 1:
        print("Final guess is:", fiveletteraccurate[0])
        gameover = 1
        return gameover
    fiveletteraccurate = []
    guesscharacter = []
    for value in guess4:
        guesscharacter.append(value)
    for i in range(5):
        if ((guesscharacter[i] == currentcharacter[i]) & (memory4[i] == '')) :
            memory4[i] = guesscharacter[i]
        elif guesscharacter[i] == '': 
            memory4[i] = ''
    # Check if a letter is found inside a word.
    for i in range(5):
        for j in range(5):
            if guesscharacter[i] == currentcharacter[j]:
                containscharacter.append(guesscharacter[i])
        for guess_char in guess4:
            if guess_char not in currentword:
                invalidchar.append(guess_char)

def score_word(word, letter_frequencies):
    return sum(letter_frequencies[letter] for letter in set(word))

# Use this on guess 5 to remove any words that contain positions already guessed.
def filteredwords():
    global filtered_words
    for word in fiveletteraccurate:
        match = True
        for i, char in enumerate(memory5):
            if char and word[i] != char:
                match = False
                break
        if match:
            filtered_words.append(word)
    return filtered_words

def fifthsetup():
    global bestword, gameover, filtered_words, fiveletteraccurate  # Removed score_word from global variables
    # Uses the data from past 4 guesses.
    columns()
    catguess()
    fiveletteraccurate = filteredwords()
    fiveletteraccurate = finetunearray(fiveletteraccurate)
    # Appends to a new array, this checks that only GREEN character in the right position are appended to the array. 
    lenarray = len(fiveletteraccurate)
    if lenarray == 1:
        print("Final guess is:", fiveletteraccurate[0])
        gameover = 1
        return
    if lenarray == 2:
        for i in range(5):
            if fiveletteraccurate[0][i] == currentcharacter[i]:
                memory5[i] = guesscharacter[i]
            elif guesscharacter[i] == '': 
                memory5[i] = ''
        for j in range(5):
            if memory5[j] == '':
                print("Final guess is:", fiveletteraccurate[1])
                gameover = 1
                return gameover
            else: 
                print("Final guess is:", fiveletteraccurate[0])
                gameover = 1
                return gameover
        exit
    elif lenarray > 2: 
        #filter = incorrectposition()
        # Score each word in the array pointers, the more points, the highest scoring is chosen.
        letter_frequencies = Counter()
        print(fiveletteraccurate)
        for word in fiveletteraccurate:
            letter_frequencies.update(set(word))
        scored_words = [(word, score_word(word, letter_frequencies)) for word in fiveletteraccurate]
        scored_words.sort(key=lambda x: x[1], reverse=True)
        bestword = scored_words[0][0]  # Use bestword instead of score_word
        return bestword

def fifthguess():
    global gameover, bestword, continuegameflag, fiveletteraccurate
    memory = []
    fifthcounter = 0
    continuegameflag = 0
    global currentcharacter
    # Checks individual letters against each other to see whether word is correct, if not we continue the game.
    for i in range(5):
        char = bestword[i]  # Use bestword instead of score_word
        memory.append(char)
        if char != currentcharacter[i]:
            continuegameflag = 1
        else:
            fifthcounter += 1
            if fifthcounter == 5:
                continuegameflag = 0
                print("Final guess is:", bestword)  # Use bestword instead of score_word
                gameover = 1

    if continuegameflag:
        # Removed our incorrect guess from the list.
        del fiveletteraccurate[0]
        # Check for any correct letters.
        for i in range(5):
            if bestword[i] == currentcharacter[i]:  # Use bestword instead of score_word
                memory6[i] = bestword[i]
            elif bestword[i] == '':  # Use bestword instead of score_word
                memory6[i] = ''
        print(memory6)
        # Chooses a random var from the remaining in list.
        lenguess6 = len(fiveletteraccurate)
        ran = random.randint(0, lenguess6 - 1)
        bestword = fiveletteraccurate[ran]    
        print("No more accurate guesses available.")
        print("Final guess is:", bestword)

def reset_variables():
    global guesscharacter, currentcharacter, containscharacter, invalidchar, fiveletteraccurate
    global memory1, memory2, memory3, memory4, memory5, scored_words, bestword, gameover, continuegameflag
    guesscharacter = []
    currentcharacter = []
    containscharacter = []
    invalidchar = []
    fiveletteraccurate = []
    memory1 = ["", "", "", "", ""]
    memory2 = ["", "", "", "", ""]
    memory3 = ["", "", "", "", ""]
    memory4 = ["", "", "", "", ""]
    memory5 = ["", "", "", "", ""]
    scored_words = ["meow"]
    bestword = ""
    gameover = 0
    continuegameflag = 0

openfile()
firstguess()
for i in range(5):
    memory2[i] = memory1[i]
if (gameover == 0):
        secondguess()
for i in range(5):
    memory3[i] = memory2[i]
if (gameover == 0):
    thirdguess()
for i in range(5):
    memory4[i] = memory3[i]
if (gameover == 0):
    fourthguess()
for i in range(5):
    memory5[i] = memory4[i]
if (gameover == 0):
    fifthsetup()
if (gameover == 0):
    fifthguess()
