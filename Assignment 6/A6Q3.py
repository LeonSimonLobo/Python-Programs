class Converter:
    def __init__(self,value,unit):
        self.value=value
        self.unit=unit
        self.measurement={"inches":1,"feet":12,"yards":36,"miles":63360,"kilometers":39370,"meters":39.37,"centimeters":0.3937,"millimeters":1/25.4}
        self.converted=self.value*self.measurement[self.unit]
    def inches(self):
          return self.converted/self.measurement["inches"]
    def feet(self):
          return self.converted/self.measurement["feet"]
    def yards(self):
          return self.converted/self.measurement["yards"]
    def miles(self):
          return self.converted/self.measurement["miles"]
    def kilometers(self):
          return self.converted/self.measurement["kilometers"]
    def meters(self):
          return self.converted/self.measurement["meters"]
    def centimeters(self):
          return self.converted/self.measurement["centimeters"] 
    def millimeters(self):
          return self.converted/self.measurement["millimeters"]
def menu():
    print("Enter the unit to which you want to convert")
    print("Or")
    choice=input("Enter 'exit' to exit:")
    return choice
def main():
      length=int(input("Enter length:"))
      measure=input("Enter unit:")
      c=Converter(length,measure)
      choice=menu()
      while choice!='exit':
            if choice=='inches':
                  print(c.inches(),"inches")
            elif choice=='feet':
                  print(c.feet(),"feet")
            elif choice=='yards':
                  print(c.yards(),"yards")
            elif choice=='miles':
                  print(c.miles(),"miles")
            elif choice=='kilometers':
                  print(c.kilometers(),"kilometers")
            elif choice=='meters':
                  print(c.meters(),"meters")
            elif choice=='centimeters':
                  print(c.centimeters(),"centimeters")
            else:
                  print(c.millimeters(),"millimeters")
            choice=menu()
if __name__=="__main__":
      main()