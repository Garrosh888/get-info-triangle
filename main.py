class Triangle():
    def __init__(self,l1,l2,l3):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
    def show_perimeter(self):
        print(f"периметр треугольника {self.length1 + self.length2 + self.length3}  ")
bob = Triangle(30,30,30)
bob.show_perimeter()
adam = Triangle(5,7,25)
adam.show_perimeter()