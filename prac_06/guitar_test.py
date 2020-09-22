"""needed help from solutions for global constant"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2020


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar1 = Guitar(name, year, cost)
    guitar2 = Guitar("guitar 2", 2012, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar1.name, 98,
                                                      guitar1.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(guitar2.name, 8,
                                                      guitar2.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar1.name,
                                                         True,
                                                         guitar1.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar2.name,
                                                         False,
                                                         guitar2.is_vintage()))


if __name__ == '__main__':
    run_tests()
