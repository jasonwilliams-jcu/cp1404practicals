import random
NUMBER_OF_LINES = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    quick_picks = int(input("enter a quick pick: "))

    for i in range(quick_picks):
        quick_pick = []
        for j in range(NUMBER_OF_LINES):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()

# needed help from solution