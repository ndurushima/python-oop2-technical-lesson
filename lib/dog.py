class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
    self.vets = []
    self.checkups = []

  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self,value):
    if type(value) is int and 0 <= value:
      self._age = value
    else:
      print("Not valid age")
  
  def add_checkup(self, vet, date, notes):
    if vet not in self.vets:
      self.vets.append(vet)
    new_checkup = {
      'vet': vet,
      'date': date,
      'notes': notes
    }
    self.checkups.append(new_checkup)
  
  def find_checkup(self, date):
    for checkup in self.checkups:
      if checkup["dates"] == date:
        print(f"Checkup on {date} with {checkup['vet']}: {checkup['notes']}")
        return
    print(f"No checkup found on {date}")
