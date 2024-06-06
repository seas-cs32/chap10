### chap10/hashfun.py -- Extracted from rk_strmatch
# Constants in Rabin-Karp's hash function
d = 256    # number of character encodings in ASCII
q = 65537  # a prime number

def hash(s):
    """Given a string s, return its hash"""
    hs = 0
    for i in range(len(s)):
        hs = ((hs * d) + ord(s[i])) % q
    return hs

# Play with the RK hash function and see if you can
# find two strings with the same hash value.
s1 = 'This is a test'
s2 = 'This is another test'
h1 = hash(s1)
h2 = hash(s2)
if h1 == h2:
    print(f'Both strings hash to {h1}!')
    print(f's1 = {s1}')
    print(f's2 = {s2}')
else:
    print('Try again :-(')
    print(f'{h1}')
    print(f'{h2}')
    