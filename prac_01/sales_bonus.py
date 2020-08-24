sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        sales = sales*.1
        print(sales)
    elif sales >= 1000:
        sales = sales*.15
        print(sales)
    else:
        print("Invalid option")
    sales = float(input("Enter sales: $"))

print("Thanks")

