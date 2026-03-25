# Complex condition checks
# Sometimes you can combine conditions 
# with AND instead of nesting if statements
#gpa = input('Enter the gpa? ')
#if float(gpa) >= .85:
#    lowest_grade = input('Enter lowest_grade? ')
#    if float(lowest_grade) >= .70:
#        print('Well done')

# AND statement
#gpa = float(input('Enter the gpa? '))
#lowest_grade = float(input('Enter lowest_grade? '))
#if gpa >= .85 and lowest_grade >= .70:
#    print('Well done')

# How AND statements are processed
# First Condition | Second Condition | Condition evaluates as
# TRUE | TRUE | TRUE
# TRUE | FALSE | FALSE
# FALSE | TRUE | FALSE
# FALSE | FALSE | FALSE

# If you  need to remember the results
# of a condition check later in your code,
# use Boolean variables as flags
honour_roll = False
gpa = float(input('Enter the gpa (Grade point Average)? '))
lowest_grade = float(input('Enter lowest_grade? '))
if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
print('honour_roll set as: ' + str(honour_roll))
# Somewhere later in your code
if honour_roll:
    print('You made honour roll')