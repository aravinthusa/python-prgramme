program:

#to find the grade of a student

class Grade:
  def __init__(self, first, second, third,
                 fourth, fifth):     
     self.first = first
     self.second = second
     self.third = third
     self.fourth = fourth
     self.fifth = fifth
  def CalGrade(self):
      average = (self.first + self.second + self.third
                            + self.fourth + self.fifth)/5 
      print(" Your average is:",average)
      if (90 <= average <= 100) :
            print(" You have obtained Grade A ")
      elif  (80 <= average < 90) :
            print(" You have obtained Grade B ")
      elif (70 <= average < 80) :
            print(" You have obtained Grade C ")
      elif  (60 <= average < 70) :
            print(" You have obtained Grade D ")
      else:
            print(" You have obtained Grade F ")
if __name__ == "__main__":
    first = int(input(" Enter the marks obtained in first subject: "))
    second = int(input(" Enter the marks obtained in second subject: "))
    third = int(input(" Enter the marks obtained in third subject: "))
    fourth = int(input(" Enter the marks obtained in fourth subject: "))
    fifth = int(input(" Enter the marks obtained in fifth subject: "))
    Grade_obj = Grade(first, second, third, fourth, fifth)
    Grade_obj.CalGrade()
    
 output:
 
 Enter the marks obtained in first subject: 54
 Enter the marks obtained in second subject: 95
 Enter the marks obtained in third subject: 65
 Enter the marks obtained in fourth subject: 75
 Enter the marks obtained in fifth subject: 45
 Your average is: 66.8
 You have obtained Grade D
