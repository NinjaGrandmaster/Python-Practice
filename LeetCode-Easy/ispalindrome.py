# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
def is_palindrome(x):
    num_str = str(x)

    if num_str == num_str[::-1]:
        return True

    return False


# is palindrome function with out string conversion
def is_palindrome_nc(x):
    # negative numbers cannot be palindromes due to "-" symbol
    if x < 0:
        return False

    temp_num = x
    reversed_num = 0
    # reverse number
    while temp_num > 0:
        reversed_num = (reversed_num * 10) + (temp_num % 10)
        temp_num = temp_num // 10  # perform integer (floor) division

    if x == reversed_num:
        return True

    return False


def main():
    print(is_palindrome(121))  # true
    print(is_palindrome(-121))  # false
    print(is_palindrome(10))  # false
    print(is_palindrome(-101))  # true

    print()

    print(is_palindrome_nc(121))  # true
    print(is_palindrome_nc(-121))  # false
    print(is_palindrome_nc(10))  # false
    print(is_palindrome_nc(-101))  # true


if __name__ == '__main__':
    main()
