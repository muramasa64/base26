 #!/usr/bin/python

import sys
import string

d = dict(zip(list(string.ascii_lowercase), [i for i in range(1, 27)]))

def base26(v):
    return 676 * d[v[0]] + 26 * d[v[1]] + d[v[2]]

if len(sys.argv) >= 2:
    for v in sys.argv[1:]:
        print("{} = {}".format(v, base26(v)))

