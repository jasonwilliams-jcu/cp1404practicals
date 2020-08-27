score = float(input("Enter score: "))

while score > 100 or score < 0:
    print("Invalid score")
    score = float(input("Enter score: "))

if score >= 50 and score < 90:
    print("passable")
elif score >= 90 and score <= 100:
    print("excellent")
else:
    print("Bad")
