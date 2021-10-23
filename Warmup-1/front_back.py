# Given a string, return a new string where the first and last chars have been exchanged.
#
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(in_str):
    # if str is a single character return it
    if len(in_str) <= 1:
        return in_str

    # get first and last characters in a string
    first_char = in_str[0]
    last_char = in_str[len(in_str) - 1]
    # get all characters between first and last characters
    temp_str = in_str[1:len(in_str) - 1]

    # return a new string with first and last characters of the input string swapped
    return last_char + temp_str + first_char


def main():
    print(front_back('code'))
    print(front_back('ab'))
    print(front_back('a'))
    print(front_back('regulation'))


if __name__ == '__main__':
    main()
