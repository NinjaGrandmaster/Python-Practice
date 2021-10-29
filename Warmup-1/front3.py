# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.
#
# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'
def front3(in_str):
    front_chars = in_str[:3]
    return front_chars + front_chars + front_chars


def main():
    print(front3('Java'))
    print(front3('Chocolate'))
    print(front3('abc'))
    print(front3('a'))


if __name__ == '__main__':
    main()
