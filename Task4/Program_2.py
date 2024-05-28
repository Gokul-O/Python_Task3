class myClass:
    a = 33

    def __init__(self):
        print("I am inside class myclass")
    def method(self):
        print("Private variable",myClass.a)

obj=myClass()
obj.method()

