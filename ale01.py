### chap10/ale01.py

def crc1_cnt(n):
    cnt_of_1s = 0

    # Add 1 to the count of 1-bits when `n`
    # is odd. Use integer-division to shift
    # down a bit, continuing until `n` is 0.
    while n != 0:
        if n % 2 == 1:
            cnt_of_1s += 1
        n = n // 2

    # Return the right value for even parity
    if cnt_of_1s % 2 == 1:
        return 1
    else:
        return 0

def crc1_xor(n):
    even_parity = 0
    n_binstr = bin(n)[2:]  # removes the leading '0b'
    #print('DEBUG: n_binstr', n_binstr)

    # INSERT some kind of loop over n_binstr and
    # the body of the loop can be done with one
    # update to `even_parity` using a bitwise operator.

    return even_parity

def test(fun, parity='even'):
    if parity == 'even':
        p, q = 0, 1
    else:
        p, q = 1, 0

    # Test the function sent in as the parameter
    if fun(0) != p:
        return 'Failed for n = 0'
    if fun(1) != q:
        return 'Failed for n = 1'
    if fun(2) != q:
        return 'Failed for n = 2'
    if fun(3) != p:
        return 'Failed for n = 3'
    if fun(16) != q:
        return 'Failed for n = 16'
    return 'PASSED our unit tests!'


def main():
    print('Testing crc1_cnt ...')
    print(test(crc1_cnt, 'even'))

    print('Testing crc1_xor ...')
    print(test(crc1_xor, 'even'))

if __name__ == '__main__':
    main()
