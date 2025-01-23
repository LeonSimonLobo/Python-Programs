measurement=['Feet','Inches','Yards','Miles','Millimeters','Centimeters','Meters','Kilometers']
feet=float(input("Enter length in feet:"))
distance=[feet,12*feet,feet/3,feet/5280,feet*304.8,feet*30.48,feet/3.281,feet/3281]
menu=0
while menu<8 and menu>=0:
    print("Distance is",distance[menu],measurement[menu])
    print("Enter 1 for distance in inches")
    print("Enter 2 for distance in yards")
    print("Enter 3 for distance in miles")
    print("Enter 4 for distance in millimeters")
    print("Enter 5 for distance in centimeters")
    print("Enter 6 for distance in meters")
    print("Enter 7 for distance in kilometers")
    print("Enter 8 to exit:")
    menu=int(input())
