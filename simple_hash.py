### chap10/simple_hash.py

def simple_hash(text):
    num = 0
    for i in range(len(text)):
        num = num * 256 + ord(text[i])
    return num

def update_hash(text, s, m, num):
    # Magnitude of the most-significant digit
    mag = 1
    for i in range(m-1):
        mag *= 256

    # Take off most-significant digit
    num = num - ord(text[s]) * mag

    # Add on a new least-significant digit
    num = num * 256 + ord(text[s + m])

    return num

def main():
    # Demonstration code for the functions above

    text = '1983'
    print(f'{text} = {simple_hash(text)}')

    text = '77719834777'
    s = 3    # Pretend we're in the middle of the match loop
    m = 4    # and the pattern string is 4 characters long
    num = simple_hash(text[s:s+m])
    print(f'{text[s:s+m]} = {num}')

    num = update_hash(text, s, m, num)
    print(f'updated hash = {num}')

    s += 1   # Verify we got the right answer
    num = simple_hash(text[s:s+m])
    print(f'{text[s:s+m]} = {num}')

    text = 'one thousand nine hundred and eighty-three'
    print(f'{text} = {simple_hash(text)}')

if __name__ == '__main__':
    main()