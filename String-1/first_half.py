# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
#
# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'
def first_half(in_str):
    mid_index = len(in_str) // 2

    return in_str[:mid_index]


def main():
    print(first_half('WooHoo'))
    print(first_half('HelloThere'))
    print(first_half('abcdef'))


if __name__ == '__main__':
    main()
