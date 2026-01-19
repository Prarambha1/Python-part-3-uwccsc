# multiple inheritance = inherit from more than one parent class
#                       C(A, B)
#
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A


class Animal:

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Prey(Animal):

    def flee(self):
        print("This animal is fleeing")


class Predator(Animal):

    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.hunt()  # ERROR: Rabbit object has no attribute 'hunt'

fish.flee()
fish.hunt()
fish.eat()
fish.sleep()
