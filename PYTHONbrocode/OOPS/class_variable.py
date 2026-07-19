# class variable = Shared variable across all instances of a class
#                 Defined within a class but outside of the constructor
#                   Allows us to share data among all objects created from that class


class Student:
    #class variable
    class_year = 2026
    num_student = 0

    def __init__(self,name,age,):
        # [NOTE] #just imagine self as the instance variables we made (here car1,2) as car1 and car2 will call this constructor and use the attributes we specify with self.____
        self.name  = name
        self.age  = age
        
        Student.num_student += 1 # we used the class-name to modify  the class-variable as the class-variable is not dependent upon the instance-variables we create outside the constructor

student1 = Student("Siddharth" , 19)
student2 = Student("Krishna" , 20)
student3 = Student("vaas" , 44)

print(student1.name)
print(student2.age)
print(student3.name)
print(student3.age)


#the class variable is common for all instances of that class (here student 1 2 )

print(Student.class_year) #we access the class variable with the class name and not with its instances , for better readability 
                          #  and to make it obvious that we are using a class variable

print(Student.num_student)



############################
print(f"My graduating class of {Student.class_year} has {Student.num_student} students in it. There names are {student1.name} (age {student1.age}) and {student2.name} (age {student2.age}) , {student3.name} (age {student3.age}) ")                                       

































































