#module = file containing code we want to include in our program
#       use "import" to include a module (build-in or our own)
#       useful to break up a large program reusable separate files


# To get help with a module use print(help("module_name"))

#import math 

import math as m   #using an alias to consice the module name for easy typing 
print(m.pi)

from math import e #this method could result in some name conflict
print(e)


#to create a module 
import temp_module

result = temp_module.square(3)
result_circumference  = temp_module.circumference(4)
print(result)
print(result_circumference)



































































 
