# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'
def string_bits(in_str):
    out_str = ""

    for i in range(len(in_str)):
        if i % 2 == 0:
            out_str += in_str[i]

    return out_str


def main():
    print(string_bits('Hello'))
    print(string_bits('Hi'))
    print(string_bits('Heeololeo'))


if __name__ == '__main__':
    main()
