def lines(a, b):
    """Return lines in both a and b"""

    # Use `set` to filter out duplicates
    lines_a = set(a.split('\n'))
    lines_b = set(b.split('\n'))

    matches = [line for line in lines_a if line in lines_b]
    return matches


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
