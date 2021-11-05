# Given a string, return a version without the first and last char, so "Hello" yields "ell".
# The string length will be at least 2.
#
# without_end('Hello') → 'ell'
# without_end('java') → 'av'
# without_end('coding') → 'odin'
def without_end(in_str):
    return in_str[1:len(in_str) - 1]


def main():
    print(without_end('Hello'))
    print(without_end('java'))
    print(without_end('coding'))


if __name__ == '__main__':
    main()
