class Bike:
    def __init__(self,model,year,color,for_sale):
        self.model = model
        self.year = year                         #These are some attributes associated with the car
        self.color = color 
        self.for_sale  = for_sale #boolean

    def drive(self):
        print(f"Your drive the {self.model} ")

    def stop(self):
        print(f"Your stop the {self.model} ")

