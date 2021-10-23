# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.
#
# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False
def array_front9(nums):

    arr_len = len(nums)

    if arr_len > 4:
        arr_len = 4

    for i in range(arr_len):
        if nums[i] == 9:
            return True

    return False


def main():
    print(array_front9([1, 2, 9, 3, 4]))
    print(array_front9([1, 2, 3, 4, 9]))
    print(array_front9([1, 2, 3, 4, 5]))
    print(array_front9([1, 2, 3, 4]))
    print(array_front9([1, 9, 3]))
    print(array_front9([1, 2]))
    print(array_front9([9]))


if __name__ == '__main__':
    main()
