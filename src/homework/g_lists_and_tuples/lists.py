def get_lowest_list_value(numbers):
    """Return the lowest number in a list using a loop (no min function)."""
    if not numbers:
        return None  # handle empty list

    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest


def get_highest_list_value(numbers):
    """Return the highest number in a list using a loop (no max function)."""
    if not numbers:
        return None  # handle empty list

    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest