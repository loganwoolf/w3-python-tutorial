a = 37
# will not work because of different type
# b = "Hi I am Logan and I am " + a 

# works
b = "Hi I am Logan and I am " + str(a)
print(b)

# templating with format()
c = "G'day my name's {} and I'm {}"
print(c.format("Loag", a))

# templating with numbered placeholders
d = "G'day my name's {1} and I'm {0}"
print(d.format(a, "Loag"))