# Given a string, return the count of the number of times that a substring length 2 appears in the string and
# also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
#
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2
def last2(input_str):
    count = 0

    if len(input_str) < 2:
        return count

    # get the length 2 substring appearing at end of input string
    last2_substring = input_str[len(input_str) - 2:]

    # iterate and count how many times target substring appears prior to the
    # ending length 2 substring
    for i in range(len(input_str) - 2):
        curr_substring = input_str[i] + input_str[i + 1]

        if curr_substring == last2_substring:
            count += 1

    return count


def main():
    print(last2('hixxhi'))
    print(last2('xaxxaxaxx'))
    print(last2('axxxaaxx'))


if __name__ == '__main__':
    main()
