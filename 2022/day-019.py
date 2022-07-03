import random
random.seed(0)

def flip(num_flips):
    """
    Flip the coin num_flips times.
    """
    heads = 0
    for i in range(num_flips):
        # if random.random() < 0.5:
        if random.choice(['H', 'T']) == 'H':
            heads += 1
    return heads/num_flips

def flip_sim(num_flips_pertrial, num_trials):
    """
    Simulate num_trials coin flips.
    """
    frac_heads = []
    for t in range(num_trials):
        frac_heads.append(flip(num_flips_pertrial))
    mean = sum(frac_heads)/len(frac_heads)
    return mean

