#nested loop = a loop within another loop (outer,inner)
#           outer loop :
#               inner loop:

#for x in range(1,10):
#    print(x, end="")    #the end attribute will print it in the same line ,, we can add "-" or"/" in the empty string too



for y in range(3): # or we can write (1,3)
    for x in range(1,10):
        print(x, end="")
    print()


"""WORKING ----
the y counter will execute the x counter for loop 3 times i.e 123456789123456789123456789 in the same line .
the print() in line 13 will print a blank space after every x counter 

OUTPUT -- 123456789
          123456789
          123456789       """



#PROJECT {rectangle with the help of symbols}

rows = int(input("Enter the # of rows: "))
column = int(input("Enter the # of column: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(column):
        print(symbol,end="")
    print()




