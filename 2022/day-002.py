# 硬币找零问题

def get_min_count_helper(total, values):
    if total == 0:
        return 0

    value_length = len(values)
    min_count = sys.maxsize
    for i in range(value_length):
        current_value = values[i]
        if current_value > total:
            continue
        rest = total - current_value
        rest_count = get_min_count_helper(rest, values)
        if rest_count == -1:
            continue
        total_count = 1 + rest_count
        if total_count < min_count:
            min_count = total_count
    if min_count == sys.maxsize:
        return -1

    return min_count


def get_min_count_of_coins_advance():
    values = [5, 3]
    total = 8
    return get_min_count_helper(total, values)

