# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
# So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place
# in both strings.
#
# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0
def string_match(a, b):
    count = 0
    # get length of the shorter string
    min_str_length = min(len(a), len(b))

    for i in range(min_str_length - 1):
        # increment count when a substring appears in the same position
        # in both input strings
        if a[i:i + 2] == b[i:i + 2]:
            count += 1

    return count


def main():
    print(string_match('xxcaazz', 'xxbaaz'))
    print(string_match('abc', 'abc'))
    print(string_match('abc', 'axc'))


if __name__ == '__main__':
    main()
