# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True
def array123(nums):
    # loop through array checking current value and following two values for the 1, 2, 3 sequence
    # return true if sequence is found else return false
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True

    return False


def main():
    print(array123([1, 1, 2, 3, 1]))
    print(array123([1, 1, 2, 4, 1]))
    print(array123([1, 1, 2, 1, 2, 3]))


if __name__ == '__main__':
    main()
