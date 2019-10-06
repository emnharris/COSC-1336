print('\n',('=' * 41),'ACC GRADEBOOK TOOL',('=' * 41),sep='')
print('=' * 100)
print('\nDirections: Enter student name followed by grades earned. To finish grade input, enter -1.\n')

#set counters
num_students = int(input('Number of students in class: '))
no_data = 0
class_average = 0
track_A = 0
track_B = 0
track_C = 0
track_D = 0
track_F = 0
#sentinel value, which stops grade input
STOP = -1

for counter in range (num_students):
    student = input('\nStudent name: ')
    grade = 0
    total = 0
    count = 0
    while grade >= 0:
        grade = int(input('Grade: '))
        total += grade
        count += 1
        # validation to prevent negative grades other than the sentinel value -1
        if grade < STOP:
            print('Data invalid; try again.')
            total -= grade
            count -= 1
            grade = 0
    if total == STOP:
        print('No grades entered for student.')
        no_data += 1       # logs students with no grades input
    else:
        average = ((total - STOP)/(count - 1))     # - 1/- STOP removes sentinel from counts so it doesn't affect average
        class_average += average
        if average >= 90:
            letter = 'A'
            message = 'Congratulate student'
            track_A += 1
        elif average >= 80:
            letter = 'B'
            message = 'Encourage student to do better next time'
            track_B += 1
        elif average >= 70:
            letter = 'C'
            message = 'Warn student they are barely passing with credit'
            track_C += 1
        elif average >= 60:
            letter = 'D'
            message = 'Put student on academic probation'
            track_D += 1
        else:
            letter = 'F'
            message = 'Suggest student drop from class'
            track_F += 1
        print('\nStudent\t\t\t\tAverage\t\tLetter grade\t\tMessage')
        print('_' * 100)
        print ('\n',student,'\t\t\t',format(average,'.1f'),'\t\t',letter,'\t\t\t',message,sep='')
print('\n',('=' * 39),'GRADE DATA FOR COURSE',('=' * 40),sep='')
print('Number of students:',num_students)
if class_average == 0:
    print('Class average: No data to calculate')
else:
    print('Class average: ',format((class_average / (num_students - no_data)),'.1f'))
    print('A\'s:',track_A)
    print('B\'s:',track_B)
    print('C\'s:',track_C)
    print('D\'s:',track_D)
    print('F\'s:',track_F)
    print('\nWARNING: You do not have any grades logged for',no_data,'student(s).\n')
