# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'
def string_splosion(input_str):
    out_str = ""

    for i in range(len(input_str)):
        # move up the original string and append to out put string
        out_str += input_str[0:i + 1]

    return out_str


def main():
    print(string_splosion('Code'))
    print(string_splosion('abc'))
    print(string_splosion('ab'))


if __name__ == '__main__':
    main()
