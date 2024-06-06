### chap10/ale02.py

def bsd_checksum(s):
    '''Given a string of 8-bit characters
       compute a 16-bit, BSD-style checksum.'''

    # Starting value for our 16-bit checksum
    checksum = 0

    # foreach character c in the input string s
        # Rotate the current checksum value right by 1 bit, where
        # rotate takes the existing least significant bit and
        # makes it the new most significant bit.

        # To this rotated value, add numerical value of
        # the current character c.

        # Store only the least-significant 16 bits of the previous
        # result as your new checksum.

    #print('DEBUG:', checksum)
    return checksum        


def main():
    # Test code
    print('Testing bsd_checksum ...')
    assert bsd_checksum('a') == 97, "Failed for s = 'a'"
    assert bsd_checksum('aa') == 32913, "Failed for s = 'aa'"
    assert bsd_checksum('bb') == 147, "Failed for s = 'bb'"
    assert bsd_checksum('test') == 16597, "Failed for s = 'test'"
    assert bsd_checksum('This is a test\n') == 11640, \
                        "Failed for s = 'This is a test\n'"
    print('PASSED our unit tests!')

if __name__ == '__main__':
    main()
