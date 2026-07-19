# keyword arguments = arguments prefixed with the names of parameters
#                                        order of the arguments doesn’t matter
#                                        helps with readability
#                                        order of arguments doesnt matter
#                                        1. positional 2. default 3. keyword 4. arbitrary



#EXAMPLE-1

def hello(greeting,title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("hello","Mr.","siddharth","singh")

#if we change the position of the arguments then itll jumble up to fix this we can assign the dedicated keyword to the argument

#hello("hello","siddharth",title="Mr.","singh") #WRONG positional arguments should always come before keyword arguments and keyword arguments should always come last
hello("hello",first="siddharth",last="singh",title="Mr.")


#EXAMPLE-2
for x in range(1,11):
    print(x, end=" ")  #end is also a keyword argument present within the "print" function
    print(x , sep="-") #sep is also a keyword argument present within the "print" functio
    
    
#EXAMPLE -3
def get_phone(country,area,first,last):
    return f"{country}---{area}---{first}---{last}"

phone_num = get_phone(country=91,area = 212 , first =457 , last = 32823)

print(phone_num)