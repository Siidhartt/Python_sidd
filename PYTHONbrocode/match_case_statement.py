# Match-case statement (known as "switch" in different programming languages) : An alternative to using many 'else if' statements
#                                                          Execute some code if a value matches a 'case'
#                                                          Benefits: cleaner and syntax is more readable


#Example -- simple program to write which day of the week it is on the basis of its date


def day_of_week(day):
    match day:

        case 1:
            return "SUNDAY"
        
        case 2:
            return "MONDAY"
        
        case 3:
            return "TUESDAY"
        
        case 4:
            return "WEDNESDAY"
        
        case 5:
            return "THURSDAY"
        
        case 6:
            return "FRIDAY"
        
        case 7:
            return "SATURDAY"
        case _ :  #Wildcard case
            return "Not a valid day"
    
print(day_of_week("ball"))
        
#Example

def is_weekend(day):
    match day:

        case "SUNDAY":
            return True
        
        case "MONDAY":
            return False
        
        case "TUESDAY":
            return False
        
        case "WEDNESDAY":
            return False
        
        case "THURSDAY":
            return False
        
        case "FRIDAY":
            return False
        
        case "SATURDAY":
            return True
        case _ : #Wildcard case
            return "Not a valid day"
    
print(is_weekend("TUESDAY"))
        

# | = or >>>> operator used when many lines have same return value
def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Monday"))


































































