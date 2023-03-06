class Caculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a + self.b


res = Caculator(1, 2).add()
print(res)