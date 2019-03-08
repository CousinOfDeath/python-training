TRIES = 10
OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'
ALREADY_GUESSED = "You have already guessed the letter: "


# DO NOT MODIFY THE initialize function
def initialize(word_list):
    """
    Takes a list of words as a parameter.
    Starting with the word in the word_list,
    starts a new game using the word.
    If the user wants to play again, starts the next
    game with the next word.
    Runs until user doesn't want to play or
    until it runs out of new words.
    """
    i = 0
    while i < len(word_list) and start_new_game(word_list[i], TRIES):
        i += 1


def obfuscate(word, letters_guessed):
    """
    Takes the current word being guessed and
    a string containing letters that user has
    tried to guess during current playthrough.

    Returns a string, that only shows letters
    that the user has guessed correctly. Return
    the guessed letter in uppercase. The letters,
    that user still has to guess are replaced with
    underscores.


    Example:
        input: 'claire','abcd'
        ouput: 'C_A___'
    Example:
        input: 'Amanda','etai'
        output: 'A_A__A'
    Example:
        input: 'Obi-Wan KENOBI','oteai'
        output: 'O_I-_A_ _E_O_I'
    """
    obfuscated = ""

    for char in word:
        if char.upper() in letters_guessed or not char.isalpha():
            obfuscated += char
        else:
            obfuscated += "_"

    return obfuscated


def start_new_game(word, max_tries):
    """
    # Arguments
    Takes a word (string) that the user has to guess,
    and max_tries (int) - the number of tries user has
    before he loses the game.


    # Description
    Before prompting the user always show the letters he still hasn't tried to guess.
    This function should prompt user for a letter, and
    check, whether the letter guessed is in the word.
    If user guessed correctly, reveal the letter to him.
    If user guessed wrong, decrease the number of tries and show the amount of tries remaining.

    Keep asking user for more letters, until he wins or loses.
    When the game ends, ask user to choose, whether they want
    to play the game again.
    If the user types 'n', return False.
    If the user types 'y', return True.
    User will only input 'n','N','y' or 'Y', so no need to handle other cases

    # Return
    Returns a boolean, stating whether user
    wants to have another game.

    Example:
        input: 'Obi-Wan Kenobi',
        execution: user wins, wants to play again,
                    types 'y' when prompted
        output: True
    Example:
        input: 'GANDALF',
        execution: user wins, doesn't want to play again,
                    types 'n' when prompted
        output: False

    """
    letters_guessed = ""
    letters_left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    max_tries = TRIES

    while max_tries > 0:
        obfuscated_word = obfuscate(word, letters_guessed)

        if obfuscated_word.find("_") == -1:
            print(obfuscated_word)
            print(GAME_WON_PHRASE)

            print(OFFER_NEXT_GAME)

            new_game = input().upper()

            if new_game == "Y":
                return 1
            else:
                return 0

        print(obfuscated_word)
        print(LETTERS_LEFT)
        print(letters_left)
        print(INPUT_PROMPT)
        print("Tries: " + str(max_tries))

        user_input = input().upper()

        if not user_input.isalpha() or len(user_input) > 1:
            print(INVALID_INPUT + "\n")
        elif user_input in letters_guessed:
            print(ALREADY_GUESSED + user_input)
        else:
            letters_guessed += user_input
            letters_left = letters_left.replace(user_input, "")
            max_tries = max_tries - 1

    print(GAME_LOST_PHRASE)


initialize(['Obi-Wan Kenobi', 'Alladin'])