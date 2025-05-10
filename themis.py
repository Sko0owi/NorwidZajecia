
import sys
def ints():
        for line in sys.stdin:
            for num in line.strip().split():
                yield int(num)
tokens = ints()
def input2():
    return next(tokens)
