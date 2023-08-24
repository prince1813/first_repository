print(2<=2 or 3>=3)
print(not(2==3 or 3==3))

a=[1,2,3,4]
b=[1,2,3,4]
print(a is b) #false because id is different
print(id(a))
print(id(b))

c=b
print(c is b)