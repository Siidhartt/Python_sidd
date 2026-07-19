#variable scope = where a variable is visible and accessible 
#scope resolution= (LEGB) local -> enclosed -> global -> Built-in

'''
def func1():
    a = 1
    print(b) # we will run into a name error as "b" is not defined in fuction 1

def func2():
    b = 2
    print(a) #SAME NAME ERROR


#we can assign multi-values to same variable in different func as its present locally inside that function itself
def func1():
    X = 1
    print(X) 

def func2():
    X = 2
    print(X) 
'''

######scope resolution= (LEGB) local -> enclosed -> global -> Built-in

#first the compiler will utilise the local variable ,IF its not present locally it will consider the enclosed variable

def func1():  #BEST EXAMPLE IS WHEN THERE'S A FUNC WITHIN A FUNC
    X = 1
    print(X) 

    def func2():  
        X = 2
        print(X) 
    func2() #this will consider x = 2 as its present locally 

#then globally and so on



