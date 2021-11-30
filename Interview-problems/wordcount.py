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
    # Word count problem
    # Given a string of words separated by whitespace calculate the count of a given target word.
    #
    # Assumptions:
    # 1. words are not case sensitive, so both lowercase and capital versions of a word should count
    # 2. no punctuation exists in the string
    # 3. if a word appears consecutively it should not count towards the count.
    #    ex. string "foo foo bar" with target word "foo" should return a count of 1

    main()
