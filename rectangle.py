class rectangle:
    def __init__(self,l,w):
      self.l= l
      self.w = w
    def area(self):
        return self.l*self.w
obj = rectangle(23,34)
print(obj.area())

class rectangle:
    def __init__(self,l,w):
      self.l= l
      self.w=w
    def area(self):
        return 2*(self.l+self.w)
obj = rectangle(23,34)
print(obj.area())



