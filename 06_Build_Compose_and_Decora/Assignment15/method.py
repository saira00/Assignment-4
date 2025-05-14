class A:
    def show(self):
        print("Show method in class A")

class B(A):
    def show(self):
        print("Show method in class B")

class C(A):
    def show(self):
        print("Show method in class C")

class D(B, C):  # Multiple inheritance
    pass

# Create object of class D
d = D()
d.show()

# Print the Method Resolution Order
print("MRO:", [cls.__name__ for cls in D.__mro__])
