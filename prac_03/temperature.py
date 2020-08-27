#refactored celsius to fahrenheight into seperate function
#refactored fahrenhieght to celsius into seperate function

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = fahren_to_cels(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = cels_to_fahren(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def cels_to_fahren(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def fahren_to_cels(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()

