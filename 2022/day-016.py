import numpy as np
import matplotlib.pyplot as plt

def regress_to_mean(num_flips, num_trials):
    """
    # Returns the number of flips required to get the mean of the
    # Bernoulli distribution.
    """
    frac_heads = []
    for t in range(num_trials):
        frac_heads.append(np.random.binomial(1, 0.5, num_flips).sum() / num_flips)

    extremes, next_trials = [], []

    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < 0.33 or frac_heads[i] > 0.66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i + 1])
    plt.plot(range(len(extremes)), extremes, 'ko', label='extremes')
    plt.plot(range(len(next_trials)), next_trials, 'k^', label='next_trials')

    plt.axhline(0.5, color='r', linestyle='--')

    plt.ylim(0, 1)
    plt.xlim(-1, len(extremes) - 1)
    plt.xlabel('Extreme Example and Next Trial')
    plt.ylabel('Fraction of Heads')
    plt.title('Regression to Mean')
    plt.legend(loc='best')
    plt.show()

regress_to_mean(15, 40)

