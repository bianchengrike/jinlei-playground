import random

from matplotlib import pyplot as plt


def flip_plot(min_exp, max_exp):
    ratios, diffs, x_axis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        x_axis.append(2 ** exp)

    for num_flips in x_axis:
        num_heads = 0
        for i in range(num_flips):
            # if random.random() < 0.5:
            if random.choice(('H', 'T')) == 'H':
                num_heads += 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads / num_tails)
            diffs.append(abs(num_heads - num_tails))
        except ZeroDivisionError:
            continue
    plt.title("Difference between Heads and Tails")
    plt.xlabel("Number of Flips")
    plt.ylabel("Abs(#Heads - #Tails)")
    plt.plot(x_axis, diffs, 'k')
    plt.figure()
    plt.title("Heads/Tails Ratios")
    plt.xlabel("Number of Flips")
    plt.ylabel("#Heads/#Tails")
    plt.plot(x_axis, ratios, 'k')
    plt.show()


random.seed(0)
flip_plot(4, 20)



