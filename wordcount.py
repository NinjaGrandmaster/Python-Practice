# input: input_str - string with words separated by whitespace
#        target - word to count in string
def word_count(input_str, target):
    words = input_str.lower().split(" ")
    target = target.lower()
    count = 0

    for i in range(len(words)):

        if i > 0:
            if words[i] == target and words[i] != words[i - 1]:
                count += 1
        else:
            if words[0] == target:
                count += 0

    return count


def main():
    test_str01 = "Hello There There is something there today there"
    count = word_count(test_str01, "There")
    print(count)


if __name__ == '__main__':
    # TODO: add full problem description and add more test cases
    main()
