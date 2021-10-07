# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True
def array123(nums):
    num_in_seq = 1
    count = 0

    for num in nums:
        if num == num_in_seq and num_in_seq <= 3:
            count += 1
            num_in_seq += 1

    if count == 3:
        return True

    return False


def main():
    print(array123([1, 1, 2, 3, 1]))
    print(array123([1, 1, 2, 4, 1]))
    print(array123([1, 1, 2, 1, 2, 3]))


if __name__ == '__main__':
    main()
