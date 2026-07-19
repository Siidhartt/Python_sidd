#indexing = accessing elements of a sequence using [] (indexing operator)
#            {SYNTAX} [star : end : step]  upto three fields to fill in

credit_number  = "1234-5678-9012-3456"

print(credit_number[3]) #output=4 (it starts with 0 like 0,1,2,3,4......)
print(credit_number[-1])  #This will give us the last digit

print(credit_number[0:4])  #This will give us the first four digits of out credit card number
print(credit_number[15:19])  #This will give us the last four digits 
print(credit_number[5:])  #This will give us the digits excpet the first four digits
print(credit_number[::2])  #This will give us every 2nd character of the string
'''
#Usage - REVERSING A STRING

reversed_digits = credit_number[::-1]   #To reverse a string STEP = -1

print(reversed_digits)


#usage
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

'''