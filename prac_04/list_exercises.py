def main():
    numbers = []
    for i in range(5):
        user_input = int(input("Enter number {}: ".format(i+1)))
        numbers.append(user_input)
    print(numbers)


main()


