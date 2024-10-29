class Triangle():
    def __init__(self,l1,l2,l3):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
        self.is_triangle = self.is_triangleTF()
    def show_perimeter(self):
        if self.is_triangle == True:
            print(f"периметр треугольника {self.length1 + self.length2 + self.length3}  ")
        else:
            print("такого треугольника нету")
    def get_longer_side(self):
        if self.length1 >= self.length2 and self.length1 >= self.length3:
            return self.length1
        elif self.length2 >= self.length1 and self.length2 >= self.length3:
            return self.length2
        else:
            return self.length3

    def get_to_ozer_sides(self):
        if self.length1 >= self.length2 and self.length1 >= self.length3:
            return (self.length2,self.length3)
        elif self.length2 >= self.length1 and self.length2 >= self.length3:
            return (self.length1,self.length3)
        else:
            return(self.length1,self.length2)

    def is_triangleTF(self):
        logest_lenth = self.get_longer_side()
        side2 = self.get_to_ozer_sides()[0]
        side3 = self.get_to_ozer_sides()[1]


        if logest_lenth < side2 + side3:
            return True
        else:
            return False
    def type_triangl_side(self):
        if self.is_triangle == False:
            print("такого треугольника нету")
        else:
            if self.length1 == self.length2 and self.length1 == self.length3:
                print("это ровностороний треугольник")
            elif self.length1 == self.length2 or self.length1 == self.length3 or self.length2 == self.length3:
                print("это ровнобедреный треугольник")
            else:
                print("разностороний треугольник")
bob = Triangle(30,30,30)
bob.show_perimeter()
bob.type_triangl_side()
bobastik = Triangle(30,30,10)
bobastik.show_perimeter()
bobastik.type_triangl_side()
adam = Triangle(5,7,25)
adam.show_perimeter()
