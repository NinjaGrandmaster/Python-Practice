# Given an array of ints length 3, return the sum of all the elements.
#
# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7
def sum3(nums):
    total_sum = 0

    for num in nums:
        total_sum += num

    return total_sum


def main():
    print(sum3([1, 2, 3]))
    print(sum3([5, 11, 2]))
    print(sum3([7, 0, 0]))


if __name__ == '__main__':
    main()
