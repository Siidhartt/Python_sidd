email = input("Enter Your email : ")

#theres a  string index method in python which can return the first instance of the character

index = email.index("@")

username= email[0:index] #or we can ignore the 0 in the indexing operator as blank space is taken as starting point itself ie [:index]
domain = email[index + 1:]  #we are using + 1 to make the output exclude the "@" itself 

print(f"Your username is {username} and Your domain is {domain}")