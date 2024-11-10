import numpy as np
from functions import *


def d_choice(m : int, d : int, batch_size = 0) -> np.array:
    '''
    This function returns, for one given experiment, the gaps of all steps in the experiment. Each step corresponds to 
    adding a new ball in the board of bins.
    '''
    # Define the arrays corresponding to the bins and the gaps.
    bins = np.zeros(m)
    gaps = np.zeros(m**2 + 1)
    
    # Start the experiment
    n = 0 
    if batch_size > 0:
        batch_bins = np.zeros(m)
        while n < m**2:
            random_bin = select_random_bin_from_d(m, d, batch_bins)
            bins[random_bin] += 1
            n += 1
            gaps[n] = calculate_gap(bins, n)

            if n%batch_size == 0:
                batch_bins = bins

    else:
        while n < m**2:
            random_bin = select_random_bin_from_d(m, d, bins)
            bins[random_bin] += 1
            n += 1
            gaps[n] = calculate_gap(bins, n)

    return gaps


def main():
    # Define the global variables
    T = 1000 # Number of times that we will repeat the experiment
    m = 50 # Number of bins
    d = 4 # Number of choices in which to chose when adding a ball to the bins
    batch_size = 10*m # Size of the batches in which the balls arrive

    total_gaps = np.zeros(m**2 + 1)
    for i in range(T):
        total_gaps += d_choice(m, d, batch_size=batch_size)

    gaps_n = total_gaps/T

    plot_gaps(gaps_n, m, batch_size=batch_size)

main()

