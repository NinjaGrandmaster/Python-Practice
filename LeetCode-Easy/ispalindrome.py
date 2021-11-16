# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is palindrome while 123 is not.
def is_palindrome(x):
    num_str = str(x)

    if num_str == num_str[::-1]:
        return True

    return False


def main():
    print(is_palindrome(121))  # true
    print(is_palindrome(-121))  # false
    print(is_palindrome(10))  # false
    print(is_palindrome(-101))  # true


if __name__ == '__main__':
    main()

