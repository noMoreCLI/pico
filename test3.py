class Test(object):

    classvar = 5

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def print(self) -> None:
        print(f"X: {self.x}, Y: {self.y}, Classvar:{self.classvar}")

    @classmethod
    def update(cls,value) -> None:
        cls.classvar = value

a = Test(1,2)
b = Test(3,4)

a.print()
b.print()

a.update(99)

a.print()
b.print()

b.update(2)
a.update(3)

a.print()
b.print()