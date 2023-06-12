def flip_case(phrase, to_swap):

    # listed_phrase = list(phrase)
    # for index, char in enumerate(listed_phrase):
    #     if char == to_swap.capitalize():
    #         listed_phrase[index] = to_swap.lower()
    #     if char == to_swap.lower():
    #         listed_phrase[index] = to_swap.capitalize()

    # stringed_phase = "".join(listed_phrase)
    # print(stringed_phase)

    result = ""
    for char in phrase:
        if char == to_swap.lower():
            result += to_swap.upper()
        elif char == to_swap.upper():
            result += to_swap.lower()
        else:
            result += char

    print(result)

    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

flip_case('Aaaahhh', 'h')