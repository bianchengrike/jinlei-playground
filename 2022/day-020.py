import random
random.seed(0)

def roll_die():
    """Returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])


def roll_n(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print(result)


