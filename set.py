a={2,1,3,4,5,7,7,7,5,9,10,9,1}
print(a)

l={1}
print(l)

m={"krishna"}
print(m)     #immutable --> string 

n={1.0}    
print(n)     #immutable --> float

# o={[1,2,3]}
# print(o)     #mutable --> list

p={(1,2,3)}
print(p)       #immutable --> tuple

a=set()
a.add(1)
a.add("prince")
a.add((1,2,3,4))
print(a)

a={1,2,3}
b={4,5,1}
a.discard(5)
print(a)

e={1,2,3}
f={4,5,6}
print(e.isdisjoint(f))
print(e.pop())
print(e.pop()) 

a={1,2,3}
a.discard(3)
print(a)
a.discard(5)
print(a)

a={1,2,3}
a.remove(3)
print(a)