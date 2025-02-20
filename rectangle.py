class rectangle:
    def __init__(self,l,w):
      self.length= l
      self.width = w
    def area(self):
        return self.l*self.w
obj = rectangle(23,34)
print(obj.area())