# 1
# class Person:
#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#     def show(self):
#         print(f"hello I'm {self.name},I'm {self.age} and my address is {self.address}")
#     def change_address(self):
#         new_address=input("enter new address: ")
#         self.address=new_address
#         print(f"your new address is {self.address}")
# ali = Person("ali",20,"tehran")
# ali.show()
# ali.change_address()
# 2
# class Cake:
#     def __init__(self,flavor,size,price):
#         self.flavor=flavor
#         self.size=size
#         self.price=price
#     def describe(self):
#         print(f"flavor: {self.flavor}, size: {self.size},price: {self.price}")
# first_cake=Cake("chocolate","large",100)
# first_cake.describe()
# 3
# class Book:
#     def __init__(self,title,author,genre,available):
#         self.title=title
#         self.author=author
#         self.genre=genre
#         self.available=available
#     def borrow(self):
#         if self.available:
#             print("you borrowed this book")
#             self.available=False
#         else:
#             print("this book is already borrowed")
# book1 = Book("harry potter", "imagination", "story", True)
# book1.borrow()
# book1.borrow()
# 4
# class SmartPhone:
#     def __init__(self, brand, model, storage, battery, camera_magapixels, os):
#         self.brand = brand
#         self.model = model
#         self.storage = storage
#         self.battery = battery
#         self.camera_magapixels = camera_magapixels
#         self.os = os
#
#     def install_app(self, app_name):
#         print(f"{app_name} installed")
#
#     def make_call(self, number):
#         print(f"calling {number}")
#
#     def take_photo(self):
#         print("take photo")
#
#     def check_battery(self):
#         if self.battery < 20:
#             print("battery is low")
#         elif self.battery == 100:
#             print("full")
#         else:
#             print(self.battery)
#
# iphone = SmartPhone("apple", "13", "1T", 100, "64mp", "ios")
# iphone.check_battery()
# iphone.take_photo()
# iphone.install_app("instagram")
# iphone.make_call("0123456789")
# 5
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         make_area=self.width*self.height
#         print(make_area)
#     def perimeter(self):
#         make_perimeter=2*(self.width+self.height)
#         print(make_perimeter)
# new= Rectangle(20, 12)
# new.area()
# new.perimeter()




#6
# class Student:
#     def __init__(self, full_name, grade_student: list):
#         self.full_name = full_name
#         self.grade_student = grade_student
#
#     def add_grade(self, score):
#         self.grade_student.append(score)
#
#     def avrage(self):
#         avg = sum(self.grade_student) / len(self.grade_student)
#         print(avg)
#
# std1 = Student('ali alavi', [10, 9, 14])
#
# std1.avrage()
# std1.add_grade(16)
# std1.avrage()


