l = [1,2,3,4,"anee"]

for i in l:
    # yeh l k paas jaaye ga starting se us k baad one by one yeh aik aik  element ko nikaale ga aur i ko assign kare ga aur us pe operations kare ga 
    print(i, type(i))

l1 = ["annie","eman","irtiza","sehrish"]

for i in l1:
    print(i, type(i))
    # jo be code for loops mai execute hoga toh wo indentation mai hona chahiye
# for else loop

for i in l1:
    print(i)
else:
    print("if for loop is able to complete itself then only else will execute")

# jab for loop successfully apne aap ko execute karta hai tab ja k else execute hoga
print("\n")
for i in l1:
    if i == "eman":
        break
    # break se break lag jaata hai, auar for loop terminate hojata hai
    print(i)

for i in l1:
    if i == "eman":
        break
    # break se break lag jaata hai, auar for loop terminate hojata hai
    print(i)
else:
    print("execute if for loop is able to complete itself")


print(l1)
for i in l1:
    if i == "eman":
        continue
    # control ko bhej do for k paaas hi immediately
    print(i)

print(l1)
for i in l1:
    if i == "eman":
        continue
    print(i)
else:
    print("This runs when the for looop will execute sucessfully")


# range function : is a generator function and helps to generate data(integers) and the upper bond is exclusive

print(list(range(5))) 
list(range(0,5,1)) #list 0 to 5 with jump 1
print(list(range(0,20,2)))
print(list(range(-10,0)))
print(list(range(-10,0,2)))


print(l1)
#derieve data in reverse order:


for i in range(len(l1)):
    print(l1[i])

for i in range(len(l1)-1,-1,-1):
    print(l1[i])


l2 = [23,45,6,7,8,544,574,3,453,23,4,5,34,36767,46434]

# derive the data present at the even index:

for i in range(2,len(l2),2):
    print(l2[i])

l3 = [1,2,3,4,5,6,7]
# sum of the elements of a given list:
sum = 0
for i in range(0,len(l3)):
    sum = sum + l3[i]

print(f"The sum is : {sum}")

# tuple

t = (1,2,3,4,4,5)
result = 0
for i in t:
    result = result + i

print(f"the sum is : {result}")

# sets:
s = {1,2,3,4,5,"anee","pwskills"}
for i in s:
    print(i)

# strings
s1 ="Aneeqah Ashraf"
for i in s1:
    print(i)


d = {"name": "aneeaqah", "course":"data science","topic":["pyhton","stats","machine learning","Deep learning", "computer vision","Natural learning processing","Resume discussion","Interview prepration"]}


# print values on the basis of keys using loops

for i in d.keys():
    print(d[i])

for i in d.values():
    print(i)
print("in items")
for i in d.items():
    print(i) #prints in the form of tuples


    





    


 