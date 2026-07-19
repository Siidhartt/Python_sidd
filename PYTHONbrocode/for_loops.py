#for loops = execute a block of code a FIXED NUMBER OF TIMES. 
# You can iterate over a range , strings, sequence etc

# [SYNTAX] for counter in range(start,end,by):


#EXAMPLE 1

credit_card = "1234-5678-9012-3456"

for x in credit_card:  #x will hold our each current position
    print(x)


for y in range(1,21):
    if y== 13:      #this will break the loop when it reaches 13
        break
    else:
        print(y)   