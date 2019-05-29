from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # Use `set` to filter out duplicates
    lines_a = set(a.split('\n'))
    lines_b = set(b.split('\n'))

    matches = [line for line in lines_a if line in lines_b]
    return matches


def sentences(a, b):
    """Return sentences in both a and b"""

    sents_a = set(sent_tokenize(a))
    sents_b = set(sent_tokenize(b))

    matches = [sentence for sentence in sents_a if sentence in sents_b]
    return matches


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    subs_a = get_substrings(a, n)
    subs_b = get_substrings(b, n)

    matches = [s for s in subs_a if s in subs_b]
    return matches


def get_substrings(s, n):
    """Return a set of all substrings of length n"""

    return {s[i:i + n] for i in range(len(s) - n + 1)}
