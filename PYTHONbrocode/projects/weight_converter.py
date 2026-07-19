weight = float(input("Enter Your Weight : "))

unit = input("KG or LB? (k or l): ")

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight , 1)}{unit}")

elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight , 1)}{unit}")
else:
    print(f"{unit} was not valid")


