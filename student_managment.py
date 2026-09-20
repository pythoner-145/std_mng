class Student:
  def __init__(self,name,std_id,marks):
    self.name = name 
    self.std_id = std_id
    self.marks = marks


  def display(self):
    return f' Name : {self.name}, Student ID : {self.std_id},Marks : {self.marks}'




class Studentmng:
 
  def __init__(self):
    self.students = []

  
  def add_std(self):
   name = input('Enter your Name : ')
   std_id = input('Enter student ID : ') 
   marks = input('Enter your makrs : ')
   new_std = Student(name,std_id,marks)
   self.students.append(new_std)

  def menu(self):
    print('Options')  
    print('='*20)
    print('1.Add student')
    print('2.View Student')
    print('3.Exit')

  def view_std(self):
    if not self.students:
      print('No Student in the system')  
      return 

    print('___Student List___')   
    for student in self.students:
      print(student.display())
      print('_'*20)

  def run(self):
    while True:
      self.menu()
      choice = input('Enter your choice : ')
      if choice == '1':
        self.add_std()

      elif choice == '2':
        self.view_std()

      elif choice == '3': 
        print('____Thank You____')
        break  


sys = Studentmng()
sys.run()
