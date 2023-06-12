import numpy


def multiply_even_numbers(nums):
    even_numbers = list(filter(lambda n: n % 2 == 0, nums))
    product = numpy.prod(even_numbers)
    print(product)


multiply_even_numbers([2, 3, 4, 5, 6])


"""Multiply the even numbers.

    >>> multiply_even_numbers([2, 3, 4, 5, 6])
    48
    
    >>> multiply_even_numbers([3, 4, 5])
    4
    
If there are no even numbers, return 1.

    >>> multiply_even_numbers([1, 3, 5])
    1
    """
