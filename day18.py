# taken from https://topaz.github.io/paste/#XQAAAQCQAwAAAAAAAAA0m0pnuFI8c/fBNApcL1Y57OO7A++5c7rDljUUsXnnkNH3NI83t8GODbivrai5cqXPdONAdkKxPsz+Two6KXbvV75e1WEtfh5scg++xfv6sZb6AlFMjN3NnotAakDYxraebTnNFRQtNP9FdNGGsJGs5EZGVqa2C3YcpcHkdfjHTiEv7yt5vldG8/cj+nl3OrqysXdTdqBO7J6Lvd5DJKMl9ZH4Jp75CFnFhNSeXJ7Ef0gx5Oi3VvhnWX0iqgMkC72YVsUzuzpzvsOwc0KrbZWoOu+DjUE9Ipl0Fj1stlAxuAftN8mFvTGgYiVE5RpdhUATg5YMMqnrEMMoLNVMQWdWQxXYFU6EQULBfRO1b2LTVf06PbR0Lc0sOrqtj5+9PaaW2k/1uPIq/pz5FGleph+/Kd8pkRKtHUERdBiS9jLkuNaTLbgLupk7J+OROLpEY3FeH6Z1Pa3Okw7wywo1b9ZfVkNkJ7T6EFywgeCe5EDtehHizV5A4FCoUO4Xr1koxjlnFAcQWk/v+Zan6LbAaA5vZP54T7Nau+ukrKgjsmPiwA7Zidw+//RPV3E=

import sys
import re


def evalstr(s, isPart2):
    while '(' in s:
        s = re.sub(r'\(([^()]*)\)',
                   lambda m: str(evalstr(m.group(1), isPart2)),
                   s)
    if isPart2:
        while '+' in s:
            s = re.sub(r'(\d+) *\+ *(\d+)',
                       lambda m: str(int(m.group(1)) + int(m.group(2))),
                       s)
    while '+' in s or '*' in s:
        # do these substitutions 1 at a time to make sure we go
        # strictly left-to-right
        s = re.sub(r'(\d+ *[+*] *\d+)',
                   lambda m: str(eval(m.group(1))),
                   s, 1)
    return int(s.strip())


def doit():
    with open('day18_input' if len(sys.argv) < 2 else sys.argv[1]) as f:
        data = list(x.strip() for x in f)
    print(sum(evalstr(ln, False) for ln in data))
    print(sum(evalstr(ln, True) for ln in data))


if __name__ == '__main__':
    doit()
