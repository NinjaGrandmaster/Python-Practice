# Given an int array length 2, return True if it contains a 2 or a 3.
#
# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False
def has23(nums):
    for num in nums:
        if num == 2 or num == 3:
            return True

    return False


def main():
    print(has23([2, 5]))
    print(has23([4, 3]))
    print(has23([4, 5]))


if __name__ == '__main__':
    main()
