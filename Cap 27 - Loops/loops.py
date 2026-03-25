# Loops

# Loop through a collection
# name -> item
# in [OBJECT, LIST]
for name in ['Christopher', 'Susan']:
    print(name)

# Looping a number of times
# range -> create a list of number for me
# index -> the item to print
for index in range(0,2):
    print(index)

# Looping with a condition
names = ['Christopher', 'Susan'] # 0,1
#index important
index = 0
#len(list) -> count
while index < len(names):
    print(names[index])
    #change the condition
    index = index + 1


