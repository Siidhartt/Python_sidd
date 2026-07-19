#Shopping cart program

foods = []
prices = []
total = 0


while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":  #lower attribute is used here to make the input in lower case as if user used "Q" to quit
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food) 