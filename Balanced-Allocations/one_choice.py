import numpy as np
from functions import *


def one_choice(m : int) -> np.array:
    '''
    This function returns, for one given experiment, the gaps of all steps in the experiment. Each step corresponds to 
    adding a new ball in the board of bins.
    '''
    # Define the arrays corresponding to the bins and the gaps.
    bins = np.zeros(m)
    gaps = np.zeros(m**2 + 1)

    # Start the experiment
    n = 0 
    while n < m**2:
        random_bin = select_random_bin(m)
        bins[random_bin] += 1
        n += 1
        gaps[n] = calculate_gap(bins, n)

    return gaps

def main():
    # Define the global variables
    T = 1000 # Number of times that we will repeat the experiment
    m = 50 # Number of bins

    total_gaps = np.zeros(m**2 + 1)
    for i in range(T):
        total_gaps += one_choice(m)

    gaps_n = total_gaps/T

    plot_gaps(gaps_n, m)

main()
