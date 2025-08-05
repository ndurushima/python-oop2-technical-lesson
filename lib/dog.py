class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
    self.vets = []
    self.checkups = []

  def get_age(self):
    return self._age
  def set_age(self,value):
    if type(value) is int and 0 <= value:
      self._age = value
    else:
      print("Not valid age")
  age = property(get_age,set_age)