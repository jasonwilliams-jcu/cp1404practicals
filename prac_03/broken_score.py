import random


def main():

    score = float(input("Enter score: "))
    print("the entered score is {} and is {}".format(score, grade_checker(score)))

    random_score = float(random.randint(0, 101))
    print("the random score is {} and is {}".format(random_score, grade_checker(random_score)))


def grade_checker(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

