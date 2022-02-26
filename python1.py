#Hello Program
name = input('Please enter your name: ')
print("Hello " + name)

#Conditional Statement
n = int(input("number: "))
if n > 0:
    print(f"n is {n} which is positive")
elif n < 0:
    print(f"n is {n} which is negative")
else:
    print("n is Zero")

#Sequence / Data Structures
#list - sequence of mutable values
names = ["Harry", 'Ron', "Hermione", 'Ginny']
print(names)
print(names[0])

#methods on list
names.append('Draco')
names.sort()
print(names)


#Tuples - sequanece of immutable vales
X = 10.0
Y = 20.0

coordinate = (X, Y)
print(coordinate)

#set - collection of unique values
numbering = set()

numbering.add(5)
numbering.add(4)
numbering.add(3)
numbering.add(1)

print(numbering)


#dict - collection of key value pairs 


#loopinnf in python

for i in range(5):
    print(i)

name = "Harry"
for char in name:
    print(char)