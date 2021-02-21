class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3,5)
print(p.x)
print(p.y)


first_name = "Eric"
last_name = "Idle"
age = 74
print(("Hello, {first_name} {last_name}. You are {age}.").format(first_name=first_name, last_name=last_name, age=age))



name = "Eric"
age = 74
print(f"Hello, {name}. You are {age}.")