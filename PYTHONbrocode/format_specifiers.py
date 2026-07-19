#format specifiers = {value:flags} SYNTAX
# format a value based on what flags are inserted 
#
#.(number)f = round to that many decimals places (fixed point)
#:(number) = allocate that many spaces to display the output
#:03 = allocate zero pad that many spaces
# :< = left justifier
# :> = right justifier
# :^ = centre align 
# :+ = use a plus  sign to indicate positive value
# := = place sign to leftmost point 
# : = insert a space before positive number 
# :, = comma separator for once tense hundreath etc places


price1 = 3.14159
price2 = -424.4124
price3 = 123.54564

print(f"Price1 is ${price1:.2f}")
print(f"Price2 is ${price2:.2f}")
print(f"Price3 is ${price3:.2f}")   

print("--------------------------------------")
#these will have 10 blank spaces to display the output
print(f"Price1 is ${price1:10}")
print(f"Price2 is ${price2:10}")
print(f"Price3 is ${price3:10}") 

print("--------------------------------------")
#these will be 0 padded 
print(f"Price1 is ${price1:010}")
print(f"Price2 is ${price2:010}")
print(f"Price3 is ${price3:010}") 

print("--------------------------------------")
#these will be left justified
print(f"Price1 is ${price1:<10}")
print(f"Price2 is ${price2:<10}")
print(f"Price3 is ${price3:<10}") 

print("--------------------------------------")
#these will be right justified
print(f"Price1 is ${price1:>10}")
print(f"Price2 is ${price2:>10}")
print(f"Price3 is ${price3:>10}") 

print("--------------------------------------")
#these will be centre justified
print(f"Price1 is ${price1:^10}")
print(f"Price2 is ${price2:^10}")
print(f"Price3 is ${price3:^10}") 


print("--------------------------------------")

print(f"Price1 is ${price1:+,.2f}")
print(f"Price2 is ${price2:+,.2f}")
print(f"Price3 is ${price3:+,.2f}") 







