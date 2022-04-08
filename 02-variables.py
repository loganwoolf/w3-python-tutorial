# variables can be re-declared
x = 4
x = "mercy"
print(x) # "mercy"

# variables can be type cast
x = str(3)
print(x) # "3"
y = int(3)
print(x)
z = float(3)
print(z)

# get the type
a = 5
b = "moose"
print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'>

# variables may only contain A-z 0-9 and _, and may not begin with a number
# convention is camelCase, PascalCase, or snake_case

# assign multiple at once

c, d, e = "cherry", "doughnut", "eucalyptus"
print(c, d, e) # >>> cherry doughnut eucalyptus

f = g = h = 19
print(f, g, h) # >>> 19 19 19

# unpack a collection (destructure array)
fruit = ["apple", "banana", "cherry"]
# i, j = fruit  # does not work due to too many values
i, j, k = fruit
print(i, j, k) # >>> apple banana cherry

print(i + j + k) # >>> applebananacherry

l = 5
m = 6
n = "john"
print(l + m) # >>> 11
# print(m + n) # error unsupported operand type
print(m, n) # >>> 6 john

o = "awesome"
p = "brutal"

def myFunc():
  p = "fantastic"
  global q
  q = "so wicked"
  print("Python is", o) # >>> Python is awesome 
  print("Python is", p) # >>> Python is fantastic

myFunc()
print("Python is", q)