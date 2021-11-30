# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def two_sum(nums, target):
    # O(n) solution
    nums_dict = {}

    for i in range(len(nums)):
        # subtract the current number from the target value
        value = target - nums[i]

        # if the target value is in the dictionary then it plus the current number would equal the target value
        # because it is the difference of the target value and current number, so we return the indexes.
        # else we add the current value to the dictionary with its index
        if value in nums_dict and nums_dict[value] != i:
            # return the index of the value form the map and the current numbers index
            return [nums_dict[value], i]
        else:
            # add current number and index to the hash map if it is not already in the hash map
            nums_dict[nums[i]] = i

    # return None if target is not possible
    return None


def main():
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))  # [1, 2]
    print(two_sum([3, 3], 6))  # [3, 3]


if __name__ == '__main__':
    main()
