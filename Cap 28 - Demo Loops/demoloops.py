# Loops

# For LOOP
people = ['Christopher', 'Susan']

# Loop through a collection
# name -> item
# in [OBJECT, LIST]
for name in people:
    print(name)

print()
# Looping a For number of times
# range -> create a list of number for me
# index -> the item to print
for index in range(0,2):
    print(index)

print()

# While LOOP
# Looping with a condition
names = ['Christopher', 'Susan'] # 0,1
#index important
index = 0
#len(list) -> count
while index < len(names):
    print(names[index])
    #change the condition
    index = index + 1
print()

