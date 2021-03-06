# You are driving a little too fast, and a police officer stops you. Write code to compute
# the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60
# or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1.
# If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day,
# your speed can be 5 higher in all cases.
#
# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0
def caught_speeding(speed, is_birthday):
    # get additional birthday speed
    if is_birthday:
        bday_buffer = 5
    else:
        bday_buffer = 0

    if speed <= (60 + bday_buffer):
        return 0
    elif (61 + bday_buffer) <= speed <= (80 + bday_buffer):
        return 1
    elif speed >= (81 + bday_buffer):
        return 2


def main():
    print(caught_speeding(60, False))
    print(caught_speeding(65, False))
    print(caught_speeding(65, True))


if __name__ == '__main__':
    main()
