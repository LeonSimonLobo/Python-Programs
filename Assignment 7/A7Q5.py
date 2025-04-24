import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
def menu():
    print("Enter 'rect' to find area and perimeter of rectangle")
    print("Enter 'circle' to find area and perimeter of circle")
    choice=input("Enter 'exit' to exit:")
    return choice
def main():
    choice=menu()
    while choice!='exit':
        if choice=='rect':
            rect=Rectangle(int(input("Enter width:")),int(input("Enter height:")))
            print(f"Rectangle Area: {rect.area()}")
            print(f"Rectangle Perimeter: {rect.perimeter()}")
        elif choice=='circle':
            circle=Circle(int(input("Enter radius:")))
            print(f"Circle Area: {circle.area()}")
            print(f"Circle Perimeter: {circle.perimeter()}")
        else:
            print("Shape not avilable!")
        choice=menu()
if __name__=='__main__':
    main()
