class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# We can get the same output by
# rewriting the previous 2 lines as
# Person('Swaroop').say_hi()
