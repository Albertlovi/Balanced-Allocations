import numpy as np
from functions import *


def partial_information_choice(m : int, d : int, k : int, batch_size = 0) -> np.array:
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
            random_bin = select_random_bin_from_d_with_k_questions(m, d, batch_bins, k)
            bins[random_bin] += 1
            n += 1
            gaps[n] = calculate_gap(bins, n)

            if n%batch_size == 0:
                batch_bins = bins

    else:
        while n < m**2:
            random_bin = select_random_bin_from_d_with_k_questions(m, d, bins, k)
            bins[random_bin] += 1
            n += 1
            gaps[n] = calculate_gap(bins, n)

    return gaps

def main():
    # Define the global variables
    T = 1000 # Number of times that we will repeat the experiment
    m = 30 # Number of bins
    d = 2 # Number of choices in which to chose when adding a ball to the bins
    k = 1 # Number of questions we can make
    batch_size = m

    total_gaps = np.zeros(m**2 + 1)
    for i in range(T):
        if (i%10 == 0):
            print(f"{i/T*100}%")
        total_gaps += partial_information_choice(m, d, k, batch_size=batch_size)

    gaps_n = total_gaps/T

    plot_gaps(gaps_n, m, plot_max=True, batch_size=batch_size)

    comparison = False
    if comparison:
        # Comparison with non-batched
        total_gaps_comparation = np.zeros(m**2 + 1)
        for i in range(T):
            if (i%10 == 0):
                print(f"{i/T*100}%")
            total_gaps_comparation += partial_information_choice(m, d, k)

        gaps_n_comparation = total_gaps_comparation/T

        plot_gaps_comparation(gaps_n, gaps_n_comparation, m, batch_size=batch_size)


main()
