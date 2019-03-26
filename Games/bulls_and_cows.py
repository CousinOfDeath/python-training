import random


def generate_cipher():
    """
    returns a random sequence of 4 unique digits as python list
    e.g.
    print(generate_cipher()) -> [5, 2, 7, 3]
    print(generate_cipher()) -> [5, 0, 3, 9]
    print(generate_cipher()) -> [3, 4, 8, 6]
    """
    cipher = []

    while len(cipher) < 4:
        random_number = random.randrange(0, 10)
        if random_number not in cipher:
            cipher.append(random_number)

    return cipher


def get_bulls_and_cows(cipher, guess):
    """
    takes 2 python lists of length 4 cipher and guess and computes the number
    of bulls and the number of cows as a 2 element tuple

    in this implementation bulls and cows will be mutually exclusive
    (a digit in the sequence can't be both a bull and a cow) and the sum of
    the two must be <= 4

    bulls: number of digits guessed correctly AND in the correct place
    cows: number of digits guessed correctly NOT in the correct place
    here are some of the test cases:
    print get_bulls_and_cows([1,2,3,4],[1,2,3,4]) -> (4, 0)
    print get_bulls_and_cows([1,2,3,4],[2,1,4,3]) -> (0, 4)
    print get_bulls_and_cows([1,2,3,4],[1,6,2,3]) -> (1, 2)
    print get_bulls_and_cows([1,2,3,4],[5,6,7,8]) -> (0, 0)
    """
    assert len(cipher) == len(guess) == 4, 'cipher and guess must be lists of length 4'

    bulls = [i for i, j in zip(cipher, guess) if i == j]
    intersect = set(cipher) & set(guess)
    cows = list(set(intersect)-set(bulls))

    return len(bulls), len(cows)


def play_game():
    # this function should use both generate_cipher and get_bulls_and_cows
    # inside and provide a command-line interface to play the game
    # while keeping the results of previous attempts as described in the pdf
    # there should be some basic validation of the user input
    # (that its a number of 4 unique digits)

    # here's an example of the game played with the cipher being [1, 3, 9, 7]
    # feel free to remove when you understood it if it feels too cumbersome :)
    # you can also play it here: http://www.mathsisfun.com/games/bulls-and-cows.html
    # pick the 0-9, 4 codes option

    # Enter your guess without spaces:
    # 1234
    # 1234 bulls: 1, cows: 1

    # Enter your guess without spaces:
    # 3945
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2

    # Enter your guess without spaces:
    # 1398
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0

    # Enter your guess without spaces:
    # 1298
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0
    # 1298 bulls: 2, cows: 0

    # Enter your guess without spaces:
    # 1397
    # 1234 bulls: 1, cows: 1
    # 3945 bulls: 0, cows: 2
    # 1398 bulls: 3, cows: 0
    # 1298 bulls: 2, cows: 0
    # 1397 bulls: 4, cows: 0

    # Congrats, You win

    guesses = []
    cipher = generate_cipher()
    won = False

    while won is False:
        print("Enter your guess without spaces:")
        guess = input()

        if not guess.isnumeric() or len(guess) is not 4 or len(set([int(i) for i in list(guess)])) is not 4:
            print("Insert 4 unique digits")
            continue

        guess_list = [int(i) for i in list(guess)]
        bulls_and_cows = get_bulls_and_cows(cipher, guess_list)

        guesses.append(f"{guess} bulls: {bulls_and_cows[0]}, cows: {bulls_and_cows[1]}")
        print("\n".join(guesses))

        if bulls_and_cows[0] is 4:
            print("Congrats, You win")
            won = True


play_game()