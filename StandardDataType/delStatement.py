#The type(), id(), and del statement:
no = 24
print("no =", no)
print("type(no) =", type(no))
print("id(no) =", id(no))
del no
print("no =", no)   #NameError: name 'no' is not defined
