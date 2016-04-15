from math import sqrt

solutions = [
        # Mine
        lambda string: reduce(lambda acc, cur: acc + cur[1], map(lambda x: (x[0], string[:x[0] + 1]), enumerate(string)), ''),
        # Others
        lambda string: reduce((lambda l, x: l+x), [string[0:i] for i in range(1, len(string)+1)]),
        lambda string: reduce(lambda x,y:x+y, [string[:i] for i in range(len(string)+1)]),
        lambda string: reduce(lambda x,y: x + string[0:string.index(y)] + y, string),
        lambda string: reduce(lambda x,y: x + x[-[i for i in range(len(x)+1) if sum(range(i+1)) == len(x)][0]:] + y, string),
        lambda string: reduce(lambda a,b: a+b, map(lambda x:[x[:i+1] for i in xrange(len(x))] , [string])[0]),
        lambda string: reduce(lambda x, y: x + string[:string.index(y)+1], string),
        lambda string: reduce(lambda x, y : x + string[:y], range(len(string)+1), ''),
        lambda string: reduce(lambda a,b: a+b, map(lambda s:[s[:i+1] for i in xrange(len(s))] , [string])[0]),
        lambda string: reduce(lambda a, b: a + string[:b], range(len(string) + 1), ""),
        lambda string: reduce(lambda x, y: x + string[:string.index(y) + 1], string    ),
        lambda string: reduce(lambda s1, s2: s1 + s2, map(lambda n: string[:n], range(len(string) + 1)), ""),
        lambda string: reduce(lambda a,b: a+b, map(lambda s:[s[:i+1] for i in xrange(len(s))] , [string])[0]),
        lambda string: reduce(lambda x,y: x+string[0:y],range(1,len(string)+1),''),
        lambda string: reduce(lambda a, b: a+b, [string[:i+1] for i in range(len(string))], ''),
        lambda string: reduce(lambda x,y:x+string[:y+1],range(len(string)),''),
        lambda string: reduce(lambda x,y : x + string[:string.find(y)+1], string),
        lambda string: reduce(lambda origin, new: origin + string[:new + 1], range(len(string)), ""),
        lambda string: reduce(lambda x, y: x + string[:y], range(len(string) + 1), ''),
        lambda string: reduce(lambda a, b: ''.join(a) + ''.join(b), [ list(string)[0:i+1] for i in range(0, len(list(string)), 1) ]),
        lambda string: reduce(lambda a, b: a + b, map(lambda n: string[:n], xrange(1, len(string)+1))),
        lambda string: reduce(lambda r, s: r + s, reduce(lambda a, s: a + [a[-1] + s], string, [''])),
        lambda string: reduce(lambda x, y: x + y, map(lambda p: string[0:p], range(1, len(string)+1))),
        lambda string: reduce(lambda x, y: x+y, (lambda o: [o[:i+1] for i,v in enumerate(o)])(string)),
        lambda string: reduce(lambda x, y: x + y, reduce(lambda x, y: x + [x[-1] + y], string, [''])),
        lambda string: reduce(lambda x, y: ''.join(string[:i] for i in range(1, len(string) + 1)) , string),
        lambda string: reduce(lambda x, (index, letter): x + string[:index] + letter, [(i, j) for i, j in enumerate(string)], ""),
        lambda string: reduce(lambda x,y : x+y, [string[:i+1] for i in range(len(string))]),
        lambda string: reduce(lambda x,y: x+string[:y[0]+1], enumerate(string), ""),
        lambda string: reduce(lambda x,y:x+y, [reduce(lambda x,y:x+y, string[:index+1]) for index, el in enumerate(string)]),
        lambda string: reduce(str.__add__,[''.join(list(string)[0:(i+1)]) for i in range(len(string))] or ['']),
        lambda string: reduce(lambda x, y: x + y,[''.join(list(string)[0:(i+1)]) for i in range(len(string))]),
        lambda string: reduce(str.__add__,(string[:i]for i in range(len(string)+1)),""),
        lambda string: reduce(lambda x, y: x + y, reduce(lambda x, y: x + [string[:len(x)]], string, [''])),
        lambda string: reduce(lambda x, y: y, '', ''.join([string[0: x[0] + 1] for x in enumerate(string)])),
        lambda string: reduce(lambda x,y: x+y, [string[:p] for p in range(len(string)+1)]),
        lambda string: reduce(lambda x, (i, e): x + string[:i+1], enumerate(string), ''),
        lambda string: reduce(lambda x, y: x+y, [string[:i] for i in range(1, len(string)+1)]),
        lambda string: reduce(lambda x, y: x+y, [string[:i+1] for i,j in enumerate(string)]),
        lambda string: reduce(lambda x,y: x + y, [string[:i+1] for i in range(len(string))]),
        lambda string: reduce(lambda a, (i,x): a + a[len(a)-i:]+x, enumerate(string), ""),
        # Official
        lambda string: reduce(lambda acc, index: acc + string[:index], xrange(len(string) + 1), str()),
        # Voodoo
        lambda string: reduce(lambda x, y: x + string[:(int(0.5*sqrt(8 * len(x) + 1) - 0.5) + 1)], string),
    ]

def string_wave(string, solution_number):
    """
    String wave takes the input and waves it out so
    it starts with the first character and repeats
    it with one more character each iteration until
    it reaches the length of the string.

    eg:
    string_wave("Puli") -> "PPuPulPuli"
    string_wave("abC") -> "aababC"
    """

    # TODO: FILL THE REDUCE STATEMENT
    # HINT1: IT SHOULD RETURN A STRING
    # HINT2: MUST BE A ONE LINER!
    # HINT3: ONLY SEND FUNC ARGUMENTS

    return solutions[solution_number](string)