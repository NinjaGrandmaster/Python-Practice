# wite a function to compute the sum of even numbers in an array
def even_sum(arr):
    sum_total = 0
    for num in arr:
        if num % 2 == 0:
            sum_total += num

    return sum_total


def main():
    print(even_sum([2, 1, 6, 9, 7]))  # 8
    print(even_sum([5, 10, 12, 18, 20]))  # 60
    print(even_sum([1, 5, 7, 13, 27]))  # 0


if __name__ == '__main__':
    main()
