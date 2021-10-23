# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'
def not_string(in_str):

    if in_str.split(" ")[0] == "not":
        return in_str

    return "not " + in_str


def main():
    print(not_string('candy'))
    print(not_string('x'))
    print(not_string('not bad'))


if __name__ == '__main__':
    main()
