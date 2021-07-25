
#
# class Dog():
#
#     # CLASS OBJECT ATTRIBUTES
#     species = "mammal"
#
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name
#
# mydog = Dog(breed = "Lab", name="Sammy")
# print(mydog.breed)
# print(mydog.name)
#
# print(mydog.species)


# class Circle():
#
#     pi = 3.14
#
#     def __init__(self, radius=1):
#         self.radius = radius
#
#     def area(self):
#         return self.radius * self.radius * Circle.pi
#
#     def set_radius(self, new_r):
#         self.radius = new_r
#
#
#
#
# myc = Circle(3)
# myc.set_radius(99)
# print(myc.area())


# class Animal():
#
#     def __init__(self):
#         print("Animal created")
#
#     def whoAmI(self):
#         print("Animal")
#
#     def eat(self):
#         print("eating")
#
#
# mya = Animal()
# mya.whoAmI()
# mya.eat()
#
#
# class Dog(Animal):
#
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#
#     def bark(self):
#         print("WOOF")
#
#     def eat(self):
#         print("dog eating")
#
#
# myd = Dog()
# myd.whoAmI()
# myd.eat()



class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, author: {}, pages: {}".format(self.title, self.author, self.pages)


    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed")


b = Book("python", "omid", 200)
print(b)
print(len(b))
del b
