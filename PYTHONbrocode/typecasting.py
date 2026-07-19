#Typecasting= The process of coverting a value of one data type to another (strings,integer,flot, boolean)
#                               Explicit vs Implicit

#EXPLICIT TYPECASTING

name = "siddharth" 
age= 19
money = 10.24293479827492734892
student= True

#Type function = tells the data type
#print(type(name))  str
#print(type(age))   int 
#print(type(money)) float
#print(type(student))   bool

    #typecasting
#1.float
age = float(age)
print(age)
    #output= 19.0 (ie float)
    #to check output type 
print(type(age))


#2.int
money= int(money)
print (money)
    #output= 10 (ie int)


#3. str
student = str(student)
print(student)
    #output = True [it is string not bool]
    #to check output 
print(type(student))

#4.bool                               IMPORTANT
age= bool(age)
print(age)
#output= True 
#Parameters :       Any number OTHER THAN 0 will be displayed as TRUE 
#                   in case of 0 --  FALSE
#                   in case of empty str ("") ---- FALSE 
#                   in case of non empty str ("djfaahsfjkhfkaj") ----- TRUE
#usage: to check if the input is 0 or not , to check if someone has filled the string(eg with their name) or not



#IMPLICIT TYPECASTING     [automatic change of data type]

x= 2
y=2.0

x= x/y    #arithmetic opperation

print(x)
print (type(x))   #Output = float 
