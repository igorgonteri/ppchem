#Q1a

atom = 'Oxygen'
atomic_number = 8
output = atom + str(atomic_number)
assert output == 'Oxygen8'

#Q1b

x = 1.1
y = 3

print(x+y)
print(x//y)
print(x*y)
print(x/y)

#Q1c

a=False
b=True
c=False

print(a and b)
print(a or b )
print(not a )
print(not b and c)
print((a and b) or c )

a = True
b = False
c = True

if a:
    if not c:
        print('Answer 1')
    elif c and b:
        print('Answer 2')
    print('Answer 3')
else:
    print('Answer 4')

#output: 'Answer 3'

#Q1e

a = 'Hydrogen'
b = 'Oxygen'
c = 1
d = 0
e = ''
f = -3
g = None

L= [a,b,c,d,e,f,g]

for i in L:
    for j in L:
        if i and j == True:
            print(f'{i} and {j} combine well')
        else:
            print(f'{i} and {j} do not combine')

#Q2a
#Q2b
#Q2c

#Q2d

list1 = [1,2,3,4,5]
print(list1[3:5])

#Q2e

print(list1[1:5:2])

#Q2f

list2 = ['Hydrogen', 'Lithium', 'Boron', 'Nitrogen', 'Fluorine']

print(list2[1:5:2])
print([list2[1],list2[3]])

#Q2h

test_even = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Sodium"]
test_odd = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine"]

def split_list(l):
    if len(l)%2==0:
        middle_index = len(l)//2
        first_half = l[0:middle_index]
        second_half = l[middle_index:len(l)]
    else:
        middle_index = len(l) // 2 + 1
        first_half = l[0:middle_index]
        second_half = l[middle_index:len(l)]
    return middle_index,first_half,second_half

print(split_list(test_even))
print(split_list(test_odd))

