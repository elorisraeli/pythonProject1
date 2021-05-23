class Robot:
    def __init__(self, n, c, a):
        self.name = n
        self.color = c
        self.age = a

    def introduce_self(self):
        print("My name is", self.name, "\n",
              "and im", self.color, "\n",
              "and im", self.age, "years old.")


r1 = Robot("Jessi", "Blue", 200)
robot2 = Robot("Morgan", "Red", 8000)
robot3 = Robot("Person Pet", "Brown", 10)

r1.introduce_self()
robot2.introduce_self()


class Person:
    def __init__(self, n, a, i, robot):
        self.name = n
        self.age = a
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def get_up(self):
        self.is_sitting = False

    def introduce_self(self):
        print("My name is", self.name, "\n",
              "and im", self.age)


p1 = Person("Dani", 50, True, robot3)
p1.introduce_self()
p1.robot_own = robot3
p1.robot_own.introduce_self()
