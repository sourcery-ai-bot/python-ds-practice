def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

    >>> number_compare(1, 1)
    'Numbers are equal'

    >>> number_compare(-1, 1)
    'Second is greater'

    >>> number_compare(1, -2)
    'First is greater'
    """
    equal, greater_than, less_than = (
        "Numbers are equal",
        "First is greater",
        "Second is greater",
    )

    if a != b:
        if a > b:
            print(greater_than)
        else:
            print(less_than)
    else:
        print(equal)


number_compare(31, -1)
