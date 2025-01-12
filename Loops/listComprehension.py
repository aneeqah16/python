l = [1,2,3,4,5,6]

l1 = list()

for i in l:
    l1.append(i**2)

print(l1)
# list comprehension
print([i**2 for i in l])


# extract the even numbers only:

print([i for i in l if i%2==0 ])