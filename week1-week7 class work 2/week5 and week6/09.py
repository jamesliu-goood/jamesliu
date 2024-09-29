class Person:
    def __init__(self):
        self.A ="James"
        self.B ="James bond"
    def PrintName(self):
        print(self.A)
        print(self._B)

P = Person()
P.A
P._B
P.PrintName()