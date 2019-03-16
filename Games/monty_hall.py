import random
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in(username='CousinOfDeath', api_key='SUaUS2N2RdsUbOJ8jG30')

# https://www.math.ucsd.edu/~crypto/Monty/monty.html


def one_try():
    """
    returns True if stick wins
    """

    doors = [1, 2, 3]
    winning_door = random.choice([1, 2, 3])
    selected_door = random.choice([1, 2, 3])

    doors.remove(winning_door)

    if winning_door is not selected_door:
        doors.remove(selected_door)

    # open a door user did not pick and ask whether he/she want's to stick with the original selection
    opened_door = random.choice(doors)

    if selected_door is winning_door:
        return True;
    else:
        return False


def run_trials(trials):
    """
    run n trials and save number of both outcomes
    """

    run_trials = 0
    winning_guesses = 0
    loosing_guesses = 0

    while run_trials <= trials:
        result = one_try()
        run_trials += 1

        if result is True:
            winning_guesses += 1
        else:
            loosing_guesses += 1

    display_sim([winning_guesses, loosing_guesses])


def display_sim(sim_result):
    """
    Make a piechart with plotly
    """

    labels = ["Won", "Lost"]

    trace = go.Pie(labels=labels, values=sim_result)

    py.plot([trace], filename='Monty Hall: stick with selection win rate')


run_trials(100)