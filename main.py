class Triangle():

    def __init__(self,l1,l2,l3):
        self.length1 = l1
        self.length2 = l2
        self.length3 = l3
        self.longest_len = self.get_longer_side()
        self.side_shorter1 = self.get_to_another_sides()[0]
        self.side_shorter2 = self.get_to_another_sides()[1]
        self.is_triangle = self.is_triangleTF()
    def show_perimeter(self):
        if self.is_triangle == True:
            print(f"периметр треугольника {self.length1 + self.length2 + self.length3}  ")
            return self.length1 + self.length2 + self.length3
        else:
            print("такого треугольника нету")
    def get_longer_side(self):
        if self.length1 >= self.length2 and self.length1 >= self.length3:
            return self.length1
        elif self.length2 >= self.length1 and self.length2 >= self.length3:
            return self.length2
        else:
            return self.length3

    def get_to_another_sides(self):
        if self.length1 >= self.length2 and self.length1 >= self.length3:
            return (self.length2,self.length3)
        elif self.length2 >= self.length1 and self.length2 >= self.length3:
            return (self.length1,self.length3)
        else:
            return(self.length1,self.length2)

    def is_triangleTF(self):
        if self.longest_len <  self.side_shorter1  +  self.side_shorter2:
            return True
        else:
            return False
    def type_triangle_side(self):#тип треугольника по длинам сторон
        type_triangle = ""
        if self.is_triangle == False:
            print("такого треугольника нету")
        else:
            if self.length1 == self.length2 and self.length1 == self.length3:
                type_triangle = "ровностороний треугольник"
                print("это ровностороний треугольник")
            elif self.length1 == self.length2 or self.length1 == self.length3 or self.length2 == self.length3:
                type_triangle = "ровнобедреный треугольник"
                print("это ровнобедреный треугольник")
            else:
                type_triangle = "разностороний треугольник"
                print("разностороний треугольник")
        return type_triangle
    def type_triangle_corner(self):
        triangle_corner = ""
        if self.is_triangle == True:
            if self.longest_len**2 == self.side_shorter1**2 + self.side_shorter2**2:
                print("right-angled triangle")#прямоугольный
                triangle_corner = "right-angled triangle"
            elif self.longest_len**2 > self.side_shorter1**2 + self.side_shorter2**2:
                print("obtuse triangle")#тупоугольный
                triangle_corner = "obtuse triangle"
            else:
                print("acute triangle")#остроугольный
                triangle_corner = "acute triangle"
        return triangle_corner

bob = Triangle(30,30,30)
bob.show_perimeter()
bob.type_triangle_side()
bob.type_triangle_corner()
bombastik = Triangle(30,30,10)
bombastik.show_perimeter()
bombastik.type_triangle_corner()
bombastik.type_triangle_side()
adam = Triangle(5,7,25)
adam.show_perimeter()
