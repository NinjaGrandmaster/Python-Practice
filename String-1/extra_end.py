# Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
# The string length will be at least 2.
#
# extra_end('Hello') → 'lololo'
# extra_end('ab') → 'ababab'
# extra_end('Hi') → 'HiHiHi'
def extra_end(in_str):
    last2_chars = in_str[-2:]

    return last2_chars + last2_chars + last2_chars


def main():
    print(extra_end('Hello'))
    print(extra_end('ab'))
    print(extra_end('Hi'))


if __name__ == '__main__':
    main()
