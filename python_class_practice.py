class Vehhicle:
    def __init__(self,color,age,seats):
        self.color = color
        self.age = age
        self.seats = seats
    def display(self):
        print(self.color, self.age, self.seats)

ob = Vehhicle("blue",3,4)
ob.display()