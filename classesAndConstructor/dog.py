class Dog:
  def __init__(self, isMale, isFat):
    self.isMale = isMale
    self.isFat = isFat
  def display(self):
    print("Is your dog a male? %s \nAnd is it fat? %s \n"%(self.isMale,self.isFat))