def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

    >>> flip_case('Aaaahhh', 'a')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'A')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'h')
    'AaaaHHH'

    """

    result = ""
    for char in phrase:
        if char == to_swap.lower():
            result += to_swap.upper()
        elif char == to_swap.upper():
            result += to_swap.lower()
        else:
            result += char

    print(result)


flip_case("Aaaahhh", "h")
