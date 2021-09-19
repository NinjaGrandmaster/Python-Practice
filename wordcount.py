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
                count += 1

    return count


def main():
    test_str01 = "Hello There There is something there today there"
    test_str02 = "It is a very nice day to is it not ok it"

    count01 = word_count(test_str01, "There")
    count02 = word_count(test_str01, "something")
    count03 = word_count(test_str02, "it")
    count04 = word_count(test_str02, "beach")

    print(count01)
    print(count02)
    print(count03)
    print(count04)


if __name__ == '__main__':
    # TODO: add full problem description
    main()
