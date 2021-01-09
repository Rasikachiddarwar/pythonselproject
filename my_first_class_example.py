# class circle:
#     no_Of_Circle = 2
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#     def area_of_circle(self):
#         area = 3.14 * self.radius* self.radius
#         return area
#
#     def perimeter_of_circle(self):
#         perimeter = 2*3.14* self.radius
#         return perimeter
#
# c1 = circle(9, "white")
# print(c1.area_of_circle())
# print(c1.perimeter_of_circle())
#
#
# c2 = circle(11, "yellow")
# print(c2.area_of_circle())
# print(c2.perimeter_of_circle())
# print("passing reference")
#
#
# cars = [1,3,2,5,4,6]
# cars.sort()
# print(cars)
# print(sorted(cars))
#
#
#
# print("after changing references")
# print(c1.area_of_circle())
# print(c1.perimeter_of_circle())





# class Person():
#
#     """Person Class definition"""
#     a = 5 # class variable
#     no_of_people = 5 # class variable
#     __not_visible_from_outside_class = 5; # hidden class variable
#     def __init__(self,firstname, lastname, eyecolor,age):
#         # Person's default values
#         self.firstname = firstname
#         self.lastname = lastname
#         self.eyecolor = eyecolor
#         self.age = age
#         self.__hidden_instance_variable = 6
#         # self.a = 7
#         no_of_people = 5
#
#     def display_fullname(self):
#         print("Full Name is %s %s and age is %d" %(self.firstname,self.lastname,self.age))
#     # def display_fullname(self,name):
#     #     print("Full Name is %s %s and age is %d" % (name, self.firstname, self.lastname, self.age))
#
#     def change_age(self,age):
#         if (age > self.age):
#             self.age = age
#
#     def read_age(self):
#         return self.age
#
#
#
#
#
# first_person = Person("Mark", "Z","brown", 54)
# print(first_person.a)
# print(first_person.firstname)
# first_person.display_fullname()
# # first_person.display_fullname("Cool")
# # first_person.__hidden_instance_variable
# print("Using hidden instance by pre-fixing with class name",first_person._Person__hidden_instance_variable)
# #first_person.__not_visible_from_outside_class
# print("Using hidden static by pre-fixing with class name",first_person._Person__not_visible_from_outside_class)
# second_person = Person(firstname = "Simon",lastname="Stuart", eyecolor="Black", age=45)
# print(second_person.firstname)
# print(type(Person.display_fullname))
# print(Person.__doc__)


# my_matrix = [[1,2,3], [4,5,6]]
# print(my_matrix(0))
# print(my_matrix(1))
# len(my_matrix)
# len(my_matrix[0])
# print(my_matrix[0][1])
# print(my_matrix[1][1])


# class Bicycle:
#         def __init__(self):
#             self.name = 5
#
# bik1 = Bicycle()
# print(bik1.name)
#

class Bicycle:
    def give_name(self):
        self.name = 5


bik1 = Bicycle()
print(bik1.name)