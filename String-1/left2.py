# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
# The string length will be at least 2.
#
# left2('Hello') → 'lloHe'
# left2('java') → 'vaja'
# left2('Hi') → 'Hi'
def left2(in_str):
    return in_str[2:] + in_str[:2]


def main():
    print(left2('Hello'))
    print(left2('java'))
    print(left2('Hi'))


if __name__ == '__main__':
    main()
