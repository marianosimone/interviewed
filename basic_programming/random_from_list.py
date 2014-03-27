import random

class ElementSelector:

    @staticmethod
    def choose_random(possibilities):
        """
        Given a list, return a random element from it

        Possible discussions:

        - Should I use a custom or a built-in Exception?
        - If the random selector would return an expcetion when asked for a non-valid range, should I catch the exception and use my own, or let it go up? (e.g.Java's Random.nextInt(0, 0))
        - Why test 10 times? Asserting randomness is actually hard, and unless you know what distribution you are aiming at, there's no "right" way to do it

        Alternative implementations:

        - some languages have built-in solutions for this problem (e.g. Python's random.choice)

        Problem variations:

        - get a random character from a String

        Tests:

        >>> ElementSelector.choose_random(None)
        Traceback (most recent call last):
        AssertionError: Can't choose from None possibilities
        >>> ElementSelector.choose_random([])
        Traceback (most recent call last):
        AssertionError: Can't choose from empty possibilities
        >>> ElementSelector.choose_random([1])
        1
        >>> all([ElementSelector.choose_random([1, 2, 3 ,4]) in [1, 2, 3, 4] for _ in range(10)])
        True
        """
        if possibilities is None:
            raise AssertionError("Can't choose from None possibilities")
        if len(possibilities) == 0:
            raise AssertionError("Can't choose from empty possibilities")
        return possibilities[random.randrange(len(possibilities))]
