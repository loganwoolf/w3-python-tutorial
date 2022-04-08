# access specific index in string, zero indexed
a = 'hello, world'
print(a[1]) # >>> e

# iterate through a string
for x in "banana":
  print(x)

# get length of string
print("String length is:", len("jjjj"))

# check for presence/absence of string in another string
print("free" in "freedom")
print("free" not in "fredrickton")

if "expensive" not in "wooly-mammoth":
  print("No, expensive is NOT present")

# modify cases 
b = "Here is a RanDOm sentence"
print(b.upper())
print(b.lower())
print(b.capitalize())
c = "   This has extra  whitespace   "
print(c.strip() +'.')
print(b.replace(' a ', ' one ').capitalize())

# split into list
print(b.split(' '))