### chap10/ale03.py
'''
This script turns the Rabin-Karp string-matching algorithm into a hash
table collision finder.
'''

import sys

# Constants in Rabin-Karp string-matching problem
d = 256    # number of character encodings in ASCII
q = 65537  # a prime number

def is_letter(c):
    if c.lower() in 'abcdefghijklmnopqrstuvwxyz':
        return True
    return False

def hash(text):
    h = 0
    for i in range(len(text)):
        h = ((h * d) + ord(text[i])) % q
    return h

def rk_strmatch(t, p):
    n = len(t)
    m = len(p)

    # Preprocessing steps

    # Compute the hash value of a 1 in the high-order position (i.e.,
    # m-1th position), where digits have radix d
    hh = 1
    for i in range(m - 1):
        hh = (hh * d) % q

    # Calculate the hash values for p and t[0:m], since the matching
    # loop needs these values as it starts
    hp = hash(p)
    ht = hash(t[:m])

    print(f'pattern hash("{p}") = {hp}')

    # Create a set to hold the collisions
    collisions = set()

    # Matching step
    for s in range(n - m + 1):
        if hp == ht:
            pass # REPLACE ME with your code.
            # TODO:
            # 1. Verify that p[0:m] and t[s:s+m] are a hash collision, 
            #    rather than a real match.
            # 2. Make sure t[s:s+m] is a standalone word by checking that 
            #    the characters immediately before and after the slice are 
            #    not letters. You can use the helper function `is_letter`.
            # 3. If both of the above are true, add t[s:s+m] to the 
            #    `collisions` set (HINT: look up "Python sets").

        if s < n - m:
            # Need to compute hash for next iteration
            ht = ((ht - (ord(t[s]) * hh)) * d
                  + ord(t[s+m])) % q
            if ht < 0:
                ht += q

    # Print collisions, if any
    if len(collisions) == 0:
        print('No collisions found')
    else:
        for crash in collisions:
            print(f'COLLISION: hash("{crash}") = {hash(crash)}')

def main():
    # Check for proper usage and grab the input strings
    if len(sys.argv) == 1:
        t = input('Text: ')
        p = input('Pattern: ')
    elif len(sys.argv) == 2:
        # Reads text from stdin
        t = sys.stdin.read()
        p = sys.argv[1]
    elif len(sys.argv) == 3:
        with open(sys.argv[1]) as f:
            t = f.read()
        p = sys.argv[2]
    else:
        sys.exit("Usage: python3 ale03.py [[text] pattern]")

    rk_strmatch(t, p)

if __name__ == '__main__':
    main()
