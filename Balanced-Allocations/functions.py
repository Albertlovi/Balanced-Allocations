import numpy as np
import matplotlib.pyplot as plt


def select_random_bin(m) -> int:
    '''
    This function selects a rondom bin from the m availeable ones.
    '''
    return np.random.randint(0, m)


def select_random_bin_from_d(m, d, bins) -> int:
    '''
    This funcition selects d bins from the m availeble ones. It then selects a rondom bin from the ones that have the 
    least load.
    '''
    random_bins = np.random.choice(range(m), size=d, replace=False)
    selected_loads = bins[random_bins]
    min_load = np.min(selected_loads)
    min_bins_indices = random_bins[selected_loads == min_load]
    
    chosen_bin_index = np.random.choice(min_bins_indices)
    return chosen_bin_index


def select_random_bin_from_d_with_k_questions(m : int, d : int, bins : np.array, k : int) -> int:
    '''
    This funcition selects d bins from the m availeble ones. It then compares the quantiles in which the selected bins 
    are, and takes a random one from the smallest quantil.
    '''
    random_bins = np.random.choice(range(m), size=d, replace=False)
    selected_loads = bins[random_bins]

    median = np.median(bins)
    percentile25 = np.percentile(bins, 25)
    percentile75 = np.percentile(bins, 75)
    under_median = random_bins[selected_loads < median]

    if k == 1:
        if len(under_median) > 0:
            random_bin = np.random.choice(under_median)
        else:
            random_bin = np.random.choice(random_bins)
    
    else:
        under_percentile25 = random_bins[selected_loads < percentile25]
        under_percentile75 = random_bins[selected_loads < percentile75]
        if len(under_percentile25) > 0:
            random_bin = np.random.choice(under_percentile25)
        elif len(under_median) > 0:
            random_bin = np.random.choice(under_median)
        elif len(under_percentile75) > 0:
            random_bin = np.random.choice(under_percentile75)
        else:
            random_bin = np.random.choice(random_bins)

    return random_bin


def calculate_gap(bins : np.array, n : int) -> float:
    '''
    This function calculates the gap (as defined in the assignment) for a particular board of bins with n balls. 
    '''
    average = n / len(bins)
    max_gap = np.max(bins - average)
    
    return max_gap


def plot_gaps(gaps : np.array, m : int, plot_max=False, batch_size=0):
    '''
    This function plots the array containing the gaps Gn as n grows.
    '''
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(gaps)), gaps, marker='o', linestyle='-', color='b',  markersize=4)

    plt.axhline(y=gaps[m], color='r', linestyle='--', label=f"Light-loaded gap: {gaps[m]}")
    plt.axhline(y=gaps[m**2], color='g', linestyle='--', label=f"Heavy-loaded gap: {gaps[m**2]}")

    plt.plot(m, gaps[m], marker='o', color='r', markersize=4)  
    plt.plot(len(gaps) - 1, gaps[m**2], marker='o', color='g', markersize=4)  

    if plot_max:
        max_value = np.max(gaps)
        round_max = round(max_value, 2)
        plt.axhline(y=max_value, color='orange', linestyle='--', label=f"Max gap: {round_max}")
    
    if batch_size > 0:
        for i in range(batch_size, len(gaps), batch_size):
            plt.axvline(x=i, color='gray', linestyle='--', linewidth=0.7, alpha=0.6, label='Batch intervals' if i == batch_size else "")

    plt.xlabel("Number of balls")
    plt.ylabel("Gn")
    # plt.title("Evolution of the gap Gn as n grows")
    plt.legend()

    plt.show()


def plot_gaps_comparation(gaps_1: np.array, gaps_2: np.array, m: int, plot_max=False, batch_size=0):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(gaps_1)), gaps_1, marker='o', linestyle='-', label="Batched one-query method", color='b',  markersize=4)
    plt.plot(range(len(gaps_2)), gaps_2, marker='o', linestyle='-', label="One-query method", color='g',  markersize=4)

    plt.axhline(y=gaps_1[m**2], color='b', linestyle='--', label=f"Heavy-loaded gap batched one-query: {gaps_1[m**2]}")
    plt.axhline(y=gaps_2[m**2], color='g', linestyle='--', label=f"Heavy-loaded gap one-query: {gaps_2[m**2]}") 

    if plot_max:
        max_value_1 = np.max(gaps_1)
        max_value_2 = np.max(gaps_2)
        round_max_1 = round(max_value_1, 2)
        round_max_2 = round(max_value_2, 2)
        plt.axhline(y=max_value_1, color='orange', linestyle='--', label=f"Max gap d-choice: {round_max_1}")
        plt.axhline(y=max_value_2, color='orange', linestyle='--', label=f"Max gap partial information: {round_max_2}")
    
    if batch_size > 0:
        for i in range(batch_size, len(gaps_1), batch_size):
            plt.axvline(x=i, color='gray', linestyle='--', linewidth=0.7, alpha=0.6, label='Batch intervals' if i == batch_size else "")
    
    plt.xlabel("Number of balls")
    plt.ylabel("Gn")
    # plt.title("Evolution of the gap Gn as n grows")
    plt.legend()

    plt.show()

def plot_gaps_probabilistic(gaps_0: np.array,
                            gaps_025: np.array, 
                            gaps_05: np.array, 
                            gaps_075: np.array,
                            gaps_1: np.array, 
                            m: int,  
                            batch_size=0):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(gaps_0)), gaps_0, marker='o', linestyle='-', label="Beta = 0", color='blue',  markersize=2)
    plt.plot(range(len(gaps_025)), gaps_025, marker='o', linestyle='-', label="Beta = 0.25", color='orange',  markersize=2)
    plt.plot(range(len(gaps_05)), gaps_05, marker='o', linestyle='-', label="Beta = 0.5", color='green',  markersize=2)
    plt.plot(range(len(gaps_075)), gaps_075, marker='o', linestyle='-', label="Beta = 0.75", color='red',  markersize=2)
    plt.plot(range(len(gaps_1)), gaps_1, marker='o', linestyle='-', label="Beta = 1", color='purple',  markersize=2)

    plt.axhline(y=gaps_0[m**2], color='blue', linestyle='--', label=f"Heavy-loaded gap: {gaps_0[m**2]}") 
    plt.axhline(y=gaps_025[m**2], color='orange', linestyle='--', label=f"Heavy-loaded gap: {gaps_025[m**2]}")
    plt.axhline(y=gaps_05[m**2], color='green', linestyle='--', label=f"Heavy-loaded gap: {gaps_05[m**2]}")
    plt.axhline(y=gaps_075[m**2], color='red', linestyle='--', label=f"Heavy-loaded gap: {gaps_075[m**2]}")
    plt.axhline(y=gaps_1[m**2], color='purple', linestyle='--', label=f"Heavy-loaded gap: {gaps_1[m**2]}")
    
    if batch_size > 0:
        for i in range(batch_size, len(gaps_1), batch_size):
            plt.axvline(x=i, color='gray', linestyle='--', linewidth=0.7, alpha=0.6, label='Batch intervals' if i == batch_size else "")
    
    plt.xlabel("Number of balls")
    plt.ylabel("Gn")
    # plt.title("Evolution of the gap Gn as n grows")
    plt.legend()

    plt.show()