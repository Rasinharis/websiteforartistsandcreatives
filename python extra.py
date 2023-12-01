# class Student:
#     def __init__(self,student_id,student_name,class_name):
#         self.student_id=student_id
#         self.student_name=student_name
#         self.class_name=class_name
# student=Student("12319689","Frank gibson","V")
# print(student.__dict__)



# class xyz:
#     __x=4
#     x=6
#     _x=9
#     print("private: ",__x)
#     print("public: ",x)
#     print("protected: ",_x)

# class abc(xyz):
#     pass
# x1=xyz()
# a1=abc()
# print(x1.x)
# print(a1._x)


n=int(input("n: "))
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*(factorial(n-1))
print(factorial(n))



# 25 202 chamber 15