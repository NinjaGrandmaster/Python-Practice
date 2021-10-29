# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

def string_times(in_str, n):
    out_str = ""

    for i in range(n):
        out_str += in_str

    return out_str


def main():
    print(string_times('Hi', 2))
    print(string_times('Hi', 3))
    print(string_times('Hi', 1))


if __name__ == '__main__':
    main()
