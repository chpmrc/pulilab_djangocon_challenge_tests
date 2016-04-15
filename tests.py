# -*- coding: utf-8 -*-

# Tests

from solutions import string_wave, solutions


def test_all(i):
    pairs = (
        ('a', 'a'),
        ('PPuPulPuli', 'Puli'),
        ('aababC', 'abC'),
        ('', ''),
    )
    try:
        for pair in pairs:
            assert pair[0] == string_wave(pair[1], i)
        print "[V] Solution %d passes! 👍" % i
    except Exception as e:
        print "[X] Solution %d fails with pair %s... 😞" % (i, pair)


if __name__ == '__main__':
    for i in range(len(solutions)):
        test_all(i)