class Student:

  def __init__(self):
    self.name = "name"

  def avg(self, math, english):
    print((math + english)/ 2)
a001 = Student()
# a001.avg(80, 70)

a001.name = "sato"
print(a001.name)
# print(a001.gender)

a002 = Student()
print(a002.name)