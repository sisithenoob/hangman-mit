# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter_checker = ""
    for letter in secret_word:
        for char in letters_guessed:
            if char == letter:
                letter_checker += char
                #print(letter_checker)
                #print(secret_word)
    
    if secret_word == letter_checker:
        return True
    else:
        return False

#test code for the is_word_guessed function
#secret_word = "onomatope"
#letter_guessed = ["p", "k", "m" , "o", "n", "a", "e", "t"]
#print(is_word_guessed(secret_word,letter_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess_word = ""
    for letter in secret_word:
        for char in letters_guessed:
            if char == letter:
                guess_word += char + ""
        if letter not in guess_word:
            guess_word += "_"
         
    return guess_word

#test code for the function get_guessed word
#secret_word = "apple"
#letter_guessed = ["p","z", "r", "l"]
#print(get_guessed_word(secret_word,letter_guessed))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_available = []

    for letter in string.ascii_lowercase:
        letters_available.append(letter)
        for char in letters_guessed:
            if letter == char:
              letters_available.remove(letter)
    
    string_letter_available = "  ".join(letters_available)
    return string_letter_available

#test code for the function get available letter
#letter_guessed = ["a", "c", "e", "p"]
#print(letter_guessed)
#print(get_available_letters(letter_guessed))
            
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass" 
    guess_letters = []
    vowels = ["a", "e", "i", "o", "u", "y"]
    num_user_guess = 6
    num_of_letter_in_word = len(secret_word)
    num_warning = 3

    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("Welcome to the game Hangman! ")
    print("I am thinking of a word that is " + str(num_of_letter_in_word) + " letters long.  ")

    

    while num_user_guess >= 0:
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        letter_available = get_available_letters(guess_letters)
        print("You have " + (str(num_user_guess)) +" guesses left. ")
        print("Available letters: " + letter_available)
        print(guess_letters)

        user_guess = input("Please guess a letter: ")
        user_guess_lower = user_guess.lower()

        if user_guess_lower not in letter_available:
            print("sorry you did not enter a letter .")
            if num_warning > 0:
                num_warning -= 1
                num_user_guess += 1
                print("You have now " + str(num_warning) + " warnings remaining")
                if num_warning == 0:
                    print("i warned you three times you lose a guess.")
                    num_user_guess -= 1
                    num_warning = 3
                
        
        if user_guess_lower in secret_word and user_guess_lower not in guess_letters:
          print("Good thinking !")
          guess_letters.append(user_guess_lower)
        elif user_guess_lower in guess_letters:
          print("you already guessed this letter !")
          if num_warning > 0:
                num_warning -= 1
                num_user_guess += 1
                print("You have now " + str(num_warning) + " warnings remaining")
                if num_warning == 0:
                    print("i warned you three times you lose a guess.")
                    num_user_guess -= 1
                    num_warning = 3
        else:
          print("oops sorry not this time")
          if user_guess_lower in vowels:
              num_user_guess -= 2
          else:
              num_user_guess -= 1

        

        print(get_guessed_word(secret_word, guess_letters))

  
        if get_guessed_word(secret_word, guess_letters) == str(secret_word):
            print("YOU WON !!!!!!")
            num_point = num_user_guess * len(secret_word)
            break
        elif num_user_guess == 0:
            print("YOU LOST !!!!!")
            print("This was the secret word : " + secret_word)
            break

      

        

        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word: str, other_word: str) -> bool:
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_stripped = my_word.replace(" ", "")
    same_char = []
    blank_stripped = []
    if len(my_word_stripped) != len(other_word):
        return False
    for index, letter in enumerate(my_word_stripped):
        if letter in string.ascii_lowercase:
            same_char.append(index)
        else:
            blank_stripped.append(index)

    mws = ''
    ow = ''
    for index_same in same_char:
        for index_dif in blank_stripped:
            if other_word[index_dif] == other_word[index_same]:
                return False
            mws += my_word_stripped[index_same]
            ow += other_word[index_same]
    
    return mws == ow

#test code for match_woth_gaps function
#print(match_with_gaps("app_e", "caped"))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list_of_match = []
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            list_of_match.append(word)
        elif match_with_gaps(my_word, word) == False:
            continue
    
    if len(list_of_match) < 1:
        print("No matches found")
    
    str_list_of_match = "  ".join(list_of_match)
    print(str_list_of_match)

#show_possible_matches("a_pl_")
            



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guess_letters = []
    vowels = ["a", "e", "i", "o", "u", "y"]
    num_user_guess = 6
    num_of_letter_in_word = len(secret_word)
    num_warning = 3

    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("Welcome to the game Hangman! ")
    print("I am thinking of a word that is " + str(num_of_letter_in_word) + " letters long.  ")

    

    while num_user_guess >= 0:
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        letter_available = get_available_letters(guess_letters)
        print("You have " + (str(num_user_guess)) +" guesses left. ")
        print("Available letters: " + letter_available)
        print(guess_letters)

        user_guess = input("Please guess a letter if you want a hint enter hint: ")
        user_guess_lower = user_guess.lower()

        if user_guess_lower == "hint":
            show_possible_matches(get_guessed_word(secret_word, guess_letters))

        if user_guess_lower not in letter_available:
            print("sorry you did not enter a letter .")
            if num_warning > 0:
                num_warning -= 1
                num_user_guess += 1
                print("You have now " + str(num_warning) + " warnings remaining")
                if num_warning == 0:
                    print("i warned you three times you lose a guess.")
                    num_user_guess -= 1
                    num_warning = 3
                
        
        if user_guess_lower in secret_word and user_guess_lower not in guess_letters:
          print("Good thinking !")
          guess_letters.append(user_guess_lower)
        elif user_guess_lower in guess_letters:
          print("you already guessed this letter !")
          if num_warning > 0:
                num_warning -= 1
                num_user_guess += 1
                print("You have now " + str(num_warning) + " warnings remaining")
                if num_warning == 0:
                    print("i warned you three times you lose a guess.")
                    num_user_guess -= 1
                    num_warning = 3
        else:
          print("oops sorry not this time")
          if user_guess_lower in vowels:
              num_user_guess -= 2
          else:
              num_user_guess -= 1

        

        print(get_guessed_word(secret_word, guess_letters))

  
        if get_guessed_word(secret_word, guess_letters) == str(secret_word):
            print("YOU WON !!!!!!")
            num_point = num_user_guess * len(secret_word)
            break
        elif num_user_guess == 0:
            print("YOU LOST !!!!!")
            print("This was the secret word : " + secret_word)
            break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)