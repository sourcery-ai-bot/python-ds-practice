def list_manipulation(lst, command, location, value=None):
    valid_commands = ["add", "remove"]
    valid_locations = ["beginning", "end"]

    if command not in valid_commands or location not in valid_locations:
        print("Invalid entry, please try again.")
        return None

    if command == "remove":
        if location == "beginning":
            del lst[0]
        elif location == "end":
            lst.pop()

    if command == "add":
        if location == "beginning":
            lst.insert(0, value)
        elif location == "end":
            lst.append(value)

    print(lst)


"""Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

family = ["Jerraill", "Sarah", "Nariayah", "Sierrah", "Lelah"]
list_manipulation(family, "add", "en", "Duke")
