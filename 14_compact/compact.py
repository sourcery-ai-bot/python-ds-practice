def compact(lst):
    """Return a copy of lst with non-true elements removed.

    >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    [1, 2, 'All done']
    """
    true_elements = list(filter(lambda ele: bool(ele), lst))
    print(true_elements)


compact([0, 1, 2, "", [], False, (), None, "All done"])
