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

#Dictionnaries

dict1= {'Boron': 'Group13', 'Sodium': 'Alkaline metal', 'Xenon': 'Noble gas', 'Astatine': 'Halogen', 'Phosphorus': 'Pnictogene'}

dict1['Sulphur'] = 'Chalcogene'
print(dict1)

#Loops

#Q3a

initial_concentration = 50
final_concentration = 3
dilution_count = 0
while initial_concentration > final_concentration +1:
    initial_concentration /= 2
    dilution_count +=1

print("The substance needs to be diluted {} times to reach the desired concentration.".format(dilution_count))

#Q3c: 10,9,8,7,6,5,4,3,2

numa = 11
while numa > 2.5:
    numa = numa - 1
    print(numa)

#Q3d: (0,2,4,6,8)/2.5

numb = 2.5
for i in range(0, 10, 2):
    pass
    print(i/numb)

#Q3e: (10.2,9.2,8.2,7.2,6.2)

numc = 10.2
while True:
    if numc < 6.2:
        break
    print(numc)
    numc -= 1

#Q3f:
#1:
#2:
#3:
#4:
collected_strings = []

for i in range(1, 5):
    if i % 2 == 0:
        for j in range(5):
            if j == 3:
                break
                collected_strings.append(str(j))
        collected_strings.append(str('F'))
    else:
        for j in range(5):
            if j == 3:
                continue
            elif j == 4:
                pass
            collected_strings.append(str(j))

for i in range(3):
    if i == 1:
        collected_strings.append("!")
        continue
    collected_strings.append("?")

collect_str = "".join(collected_strings)
print(f'Collected string is {collect_str}')

#Q3g

n = 10
i = 10
while i > 0:
    if i % 2 == 0:
        i=i/2
    else:
        i=i-1

#Q4b

def test_function(inp_list, tgts):
    found_tgts = []
    for tgt in tgts:
        if tgt in inp_list:
            found_tgts.append(tgt)
    return found_tgts

import random

MAX_SIZE = 10000000 # This is the maximum value of the numbers in the list
MAX_TGT_VALUE = 10000000 # This is the maximum value of the target numbers
LENGTH = 10000000 # This is the length of the list

# Here we declare a list of random numbers and a list of random target numbers
random_integers = [random.randint(0, MAX_SIZE) for i in range(LENGTH)]
target_integers = [random.randint(0, MAX_TGT_VALUE) for i in range(10)]
targets_found = []

comparison_counter = 0

for j in target_integers:
    for i in range(0,len(random_integers)):
        if random_integers[i] == j:
            targets_found.append(j)
            comparison_counter += 1

        elif i == len(random_integers):
            comparison_counter += 1
            break
        else:
            comparison_counter += 1

print(comparison_counter)
print(targets_found)
assert targets_found == test_function(random_integers, target_integers)
print(f'Your code worked! Average number of comparisons per search = {comparison_counter/len(target_integers)}')

#Q4e