menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}


cart = []
total = 0
print("=================MENU=================")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("======================================")



while True:
    food = input("Select items (q to quit): ")

    if food.lower() == "q":
        break
    elif menu.get(food) is None:
        print("Enter valid items only")
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)


print()
print("======================================")
print()
print(f"CART -- {cart}")
print(f"TOTAL -- {total}")        


