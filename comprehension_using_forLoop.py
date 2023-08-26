#even numbers between 0 and 10
a=[]
for i in range(10):
    if i%2==0:
        a.append(i)
print(a)

#using comprehension
b=[i for i in range(10) if (i%2==0)]
print(b)

a=[1,2,3,4]
b=["krishna","rohan","sohan","ranbir"]
c=["kumar","aggarwal","malhotra","kapoor"]
for i,j,k in zip(a,b,c):
    print(i,j,k, sep=",")