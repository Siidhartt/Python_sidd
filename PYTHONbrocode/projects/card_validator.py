#Objective:
# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

sum_odd_digits  = 0
sum_even_digits = 0
total = 0

#Step 1
card_num = input("Enter the card number: ")
card_num = card_num.replace("-","").replace(" ","")


#step2
card_num = card_num[::-1] #to reverse the string so that we can add odd places right to left

for x in card_num[::2]:  #we will itirate over every 2nd digit 
    sum_odd_digits += int(x)  #typecasting x as an integer to add it 

#step 3

for y in card_num[1::2] :
    y = int(y)*2

    if y>= 10:  #if y is a two digit number 
        sum_even_digits += (1 + (y%10)) #adding the distinct digits to get a singledigit number {y%10 will give us remainder}
    else:
        sum_even_digits += y  

    
#step 4

total = sum_odd_digits + sum_even_digits

#step 5
if total % 10 == 0:
    print("VALID")

else:
    print("INVALID")











































































