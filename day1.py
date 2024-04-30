# class Humen:
#     pass


# class Humen:
#     legs=2
#     eyes=2

#     def walking():
#         print("Humen can walk")

#     def talking():
#         print("humen can talk")

# anu=Humen        ####anu->object
# print(anu.legs)
# anu.talking()
# print(".......................")
# kiran=Humen
# print(kiran.legs)
# kiran.talking()


###SELF
# ***********
# class Humen:
#     legs=2
#     eyes=2

#     def walking(self):
#         print("Humen can walk")

#     def talking(self):
#         print("humen can talk")

# anu=Humen()       ####anu->object
# print(anu.legs)
# anu.talking()
# print(".......................")
# kiran=Humen()
# print(kiran.legs)
# kiran.talking()


# class Humen:
#     legs=2
#     eyes=2

# anu=Humen()        ####anu->object
# print(anu.legs)
# print(".......................")
# kiran=Humen()
# print(kiran.legs)
# print(".......................")
# kiran.legs=3
# print(kiran.legs)
# print(anu.legs)
# print(".......................")
# Humen.legs=4
# print(anu.legs)
# print(kiran.legs)


##<<<<<<<<<<<<CONSTRUCTOR>>>>>>>>>>>>>>>>>>>> 

# class Humen:
#     legs=2
#     eyes=2

#     def __init__(self):  # NON PARAMETERIZED CONSTRUCTOR
#         print("I an humen")

#     def walking(self):
#         print("Humen can walk")

#     def talking(self):
#         print("humen can talk")

# anu=Humen()       
# print(anu.legs)
# anu.talking()
# print(".......................")
# kiran=Humen()
# print(kiran.legs)
# kiran.talking()


# class Student:

#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age

# s1 = Student(1, "Sara", 10)
# s2 = Student(2, "Jose", 20)

# print(getattr(s1, "id")) 
# print(getattr(s1, "name")) 
# print(getattr(s1, "age")) 

# print(getattr(s2, "name")) 
# setattr(s2, "name", "Kris")
# print(getattr(s2, "name"))


# ##      SUPER
# class A:
#     def __init__(self):
#         print('welcome')
    
#     def __init__(sef):
#         print('show')

# class A1(A):
#     def __init__(self):
#         print("welcome!")

#     def show(self):
#         super().show()
#         print('SHOW!')

# a=A1
# a.show()