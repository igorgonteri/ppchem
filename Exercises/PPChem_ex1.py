#exercise 1.1

my_string = "2cfo6njs[pwi2r3adcvy"
print(my_string[0:10:2])

#exercise 1.2

a = 5
b = 6
print(a + b)

#exercise 1.3

sentence = 'Sober Physicists Don’t Find Giraffes Hiding In Kitchens'
l = []
for i in sentence:
    if i.isupper() == True:
        l.append(i)
print(l)

#exercise 1.4

chem = {'NaOH':'HCl', 'KOH': 'H2SO4', 'Ca(OH)2': 'HNO3'}
chem2 = {'Base': ['NaOH', 'KOH', 'Ca(OH)2'], 'Acids': ['HCl','H2SO4','HNO3']}
chem2['Base'].append('NH4OH')
print(chem2)

#Pathlib intro

from pathlib import Path

p = Path('.')
print(p.resolve())

for file in p.iterdir():
    print(file)

new_dir = p / 'PPChem_ex2'
new_dir.mkdir(exist_ok=True)
print(new_dir.exists())

new_file = new_dir / 'new_file.txt'
new_file.touch()

print(new_file.exists())
new_file.unlink()

new_dir.rmdir()

print(new_dir.exists())

#exercise 2.1

p = Path('.')
print(p.resolve())
new_dir = p/ 'ex_folder'
new_dir.mkdir(exist_ok=True)
print(new_dir.exists())

new_file = new_dir/'ex_file.py'
new_file.touch()



#exercise 2.2










