# What is this?

A tester for [Pulilab's DjangoCon 2016 challenge](http://www.pulilab.com/djangocon/) solutions.

# Usage

`python tests.py`

# But...Why?

Because it's always nice to look at problems (and solutions) from different perspectives and I wanted to see how the other solutions would handle the different cases. Surprisingly most of the solutions fail with empty strings (an empty string is still a string!). Nevertheless you can learn **a lot** from all of them!

# Anything else?

Well...this solution returns a list when fed a 1-character string:

`reduce(lambda a, b: ''.join(a) + ''.join(b), [ list(string)[0:i+1] for i in range(0, len(list(string)), 1) ]),`

Pulilab's tests were "flexible" I guess 😁
