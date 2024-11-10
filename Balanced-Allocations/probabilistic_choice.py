import numpy as np
import random
from functions import *


def probabilistic_choice(m : int, beta : float, batch_size = 0) -> np.array:
    '''
    This function returns, for one given experiment, the gaps of all steps in the experiment. Each step corresponds to 
    adding a new ball in the board of bins. To do so, it uses the one_choice method with probability beta and the 
    two_choice method with probability 1 - beta.
    '''
    # Define the arrays corresponding to the bins and the gaps.
    bins = np.zeros(m)
    gaps = np.zeros(m**2 + 1)

    # Start the experiment
    n = 0 
    if batch_size > 0:
        batch_bins = np.zeros(m)
        while n < m**2:
            if random.random() < beta:
                random_bin = select_random_bin(m)
            else:
                random_bin = select_random_bin_from_d(m, 2, batch_bins)
            
            bins[random_bin] += 1
            n += 1
            gaps[n] = calculate_gap(bins, n)

            if n%batch_size == 0:
                batch_bins = bins

    else:
        while n < m**2:
            if random.random() < beta:
                random_bin = select_random_bin(m)
            else:
                random_bin = select_random_bin_from_d(m, 2, bins)
            
            bins[random_bin] += 1
            n += 1
            gaps[n] = calculate_gap(bins, n)

    return gaps


def main():
    # Define the global variables
    T = 1000 # Number of times that we will repeat the experiment
    m = 50 # Number of bins
    beta = 0.5 # Probability for the probabilistic method
    batch_size = 10*m

    total_gaps_0 = np.zeros(m**2 + 1)
    for i in range(T):
        if (i%100 == 0):
            print(f"{i/T*100}%")
        total_gaps_0 += probabilistic_choice(m, 0, batch_size=batch_size)
    
    gaps_n_0 = total_gaps_0/T

    total_gaps_025 = np.zeros(m**2 + 1)
    for i in range(T):
        if (i%100 == 0):
            print(f"{i/T*100}%")
        total_gaps_025 += probabilistic_choice(m, 0.25, batch_size=batch_size)
    
    gaps_n_025 = total_gaps_025/T

    total_gaps_05 = np.zeros(m**2 + 1)
    for i in range(T):
        if (i%100 == 0):
            print(f"{i/T*100}%")
        total_gaps_05 += probabilistic_choice(m, 0.5, batch_size=batch_size)
    
    gaps_n_05 = total_gaps_05/T

    total_gaps_075 = np.zeros(m**2 + 1)
    for i in range(T):
        if (i%100 == 0):
            print(f"{i/T*100}%")
        total_gaps_075 += probabilistic_choice(m, 0.75, batch_size=batch_size)
    
    gaps_n_075 = total_gaps_075/T

    total_gaps_1 = np.zeros(m**2 + 1)
    for i in range(T):
        if (i%100 == 0):
            print(f"{i/T*100}%")
        total_gaps_1 += probabilistic_choice(m, 1, batch_size=batch_size)
    
    gaps_n_1 = total_gaps_1/T
    
    plot_gaps_probabilistic(gaps_n_0, gaps_n_025, gaps_n_05, gaps_n_075, gaps_n_1, m, batch_size=batch_size)

main()