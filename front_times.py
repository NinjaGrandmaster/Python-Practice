# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
# or whatever is there if the string is less than length 3. Return n copies of the front;
#
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'
def front_times(input_str, n):
    out_str = ""

    if len(input_str) < 3:
        front = input_str
    else:
        front = input_str[0:3]

    for i in range(n):
        out_str += front

    return out_str


def main():
    print(front_times('Chocolate', 2))
    print(front_times('Chocolate', 3))
    print(front_times('Abc', 3))


if __name__ == '__main__':
    main()
