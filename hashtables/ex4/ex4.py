def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = {}
    sort_list = sorted(a, reverse=True)

    for item in sort_list:
        if item >= 0 and item not in numbers:
            numbers[item] = 0
        if item < 0 and -item in numbers:
            numbers[-item] += 1

    # print(numbers)
    result = []
    for number in numbers:
        if numbers[number] > 0:
            result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
