# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def find_longest_with_at_most(string: str, k: int) -> str:
    if not string or len(string) == 1:
        return string

    seen = set()
    start_last_seen = 0
    longest_start = longest_end = 0
    start_last_seen = current_start = 0

    for i, char in enumerate(string):
        if char in seen:
            if char == string[current_start]:
                start_last_seen = i
        else:
            if len(seen) < k:
                seen.add(char)
            else:
                if i - current_start > longest_end - longest_start:
                    longest_start = current_start
                    longest_end = i
                seen = seen - set(string[current_start]) | set(char)
                current_start = start_last_seen = start_last_seen + 1
    if seen and len(string) - current_start > longest_end - longest_start:
        longest_end = len(string)

    return string[longest_start:longest_end]

import pytest

@pytest.mark.parametrize(('string', 'k', 'expected'), [
    ('a', 2, 'a'),
    ('ab', 1, 'a'),
    ('ab', 2, 'ab'),
    ('abcba', 2, 'bcb'),
    ('abac', 3, 'abac'),
    ('aaaaavaaaaaac', 1, 'aaaaaa'),
    ('', 2, ''),
])
def test(string, k, expected):
    assert find_longest_with_at_most(string, k) == expected
