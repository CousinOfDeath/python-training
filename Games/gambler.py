import random


def one_try(coins, goal):
    """
    place bets while there is at least 1 coin left
    probability of winning is 50%, increment/decrement
    coins after each run, return tuple
    (number_of_bets: int, won: boolean)
    """
    number_of_bets = 0
    won = False

    while coins > 0 and coins < goal:
        number_of_bets += 1
        choice = random.choice([0, 1])
        if choice == 1:
            coins += 1
        else:
            coins -= 1

    if coins == goal:
        won = True

    return number_of_bets, won


def run_n_trials(coins, goal, trials):
    """
    Run simulation with n trials
    return list of tuples (number_of_bets: int, won: boolean)
    """
    repeated_tries = []
    repeated = 0
    while repeated <= trials:
        repeated += 1
        return_value = one_try(coins, goal)
        repeated_tries.append(return_value)

    return repeated_tries


def get_average_winrate(results):
    """
    Calculate average win rate based on the data returned
    from run_n_trials
    """
    total_games = sum([i[0] for i in results])
    total_wins = sum([i[0] for i in results if i[1] is True])
    print(round((total_wins / total_games) * 100, 2))



print(get_average_winrate(run_n_trials(10, 20, 100)))