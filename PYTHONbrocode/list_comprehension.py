# List comprehension = A concise way to create lists in Python
#                                        Compact and easier to read , than traditional loops
#                                    FORMULA -- [expression for value in iterable if condition]


#Traditional loop 

doubles = []
for x in range (1 ,11):
    doubles.append(x *2)

print(doubles)


#Or we can use list comprehension

         #doubles = [expression for value in iterable if condition]

doubles = [x*2 for x in range(1,11)]
print(doubles)


#Example
fruits = ["apple" , "orange", "banana" , "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

#Example with condition

numbers = [1,-2,3,-4,5,-6 , 12, 18]
 
positive_nums = [num for num in numbers  if num>=0 ] #the first "num" is writen since we need to give it an expression and if we are not modifying its value we can just return the value of "num"
negative_nums = [num for num in numbers  if num<=0 ]
even_nums = [num for num in numbers if num%2 == 0]
odd_nums = [num for num in numbers if num%2 == 1]
print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

#EXERCISE

grades = [ 86,64,44,34,89,92]

passing_grades = [passing for passing in grades if passing>=60 ]
print(passing_grades)

print(f"total number of students passes: {len(passing_grades)}")

























