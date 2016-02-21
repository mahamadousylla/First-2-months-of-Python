print('Mahamadou Sylla')

Grades = ['A', 'B', 'C', 'D', 'E']
NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4

from random import *

##########c.1###########

def generate_answers():
    result = ''
    for number in range(0, NUMBER_OF_QUESTIONS):
        result+= choice(Grades[0:NUMBER_OF_CHOICES])
    return result
ANSWERS = generate_answers()
    
##########c.2 AND c.3###########

from collections import namedtuple

Student = namedtuple('Student', 'name answers scores total')

##def random_students():
##    Students = []
##    for number in range(0, NUMBER_OF_STUDENTS):
##        temp = generate_answers()
##        Students.append(Student(randrange(11111, 99999), temp))
##    return Students
##print(random_students())

def random_students():
    Students = []
    for number in range(0, NUMBER_OF_STUDENTS):
        temp = generate_answers()
        scores = []
        total=0
        for grade in temp:
            index = 0
            if grade == ANSWERS[index]:
                scores.append(1)
                total+=1
            else:
                scores.append(0)
            index+=1
        Students.append(Student(randrange(11111, 99999), temp, scores, total))
    return Students
##print(random_students())
print('\n\n\n\n')






##########c.4###########

def generate_weighted_student_answer(aString):
    Grade = Grades[0:NUMBER_OF_CHOICES]
    Grade.append(aString)
    return choice(Grade)

def random_students2():
    Students = []
    for number in range(0, NUMBER_OF_STUDENTS):
        ANSWERS = generate_answers()
        scores = []
        total=0
        x=''
        for letter in ANSWERS:
            new_letter = generate_weighted_student_answer(letter)
            x+=new_letter
        for grade in x:
            index = 0
            if grade == ANSWERS[index]:
                scores.append(1)
                total+=1
            else:
                scores.append(0)
            index+=1      
        Students.append(Student(randrange(11111, 99999), x, scores, total))
    return Students             
##print(random_students2())

def sorting(student):
    return student.total

allstudents = random_students2()
allstudents.sort(key=sorting, reverse=True)
print(allstudents[:11])

def avg():
    x=0
    for student in random_students():
        x+=student.total
    return (x/NUMBER_OF_STUDENTS)
##print(avg())

def avg2():
    x=0
    for student in random_students2():
        x+=student.total
    return (x/NUMBER_OF_STUDENTS)
##print(avg2())

##########c.5###########


def question_weights(listOfstudents):
    count=0
    i=0
    for n in range(0, NUMBER_OF_QUESTIONS):
        for student in listOfstudents:
            for number in student.scores:
                if number == 0:
                    count+=1
                print(count)
##print(question_weights([Student(name=88169, answers='BCBABBDBDBDBBABADBBA', scores=[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], total=1), Student(name=13746, answers='BBBDDABBDAAADDDCABDD', scores=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], total=1), Student(name=68685, answers='ABBCBCBDABAAAAACDCCB', scores=[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], total=2), Student(name=43402, answers='BACDAABABCCACCBBDCCB', scores=[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], total=2), Student(name=27055, answers='AABCDBADBAAACBACBCBB', scores=[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], total=2), Student(name=45019, answers='CAACABBCADBACAACCBBD', scores=[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], total=2), Student(name=76821, answers='AAABBCAABADBBCDABABD', scores=[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], total=2), Student(name=26793, answers='CCDCCBAACBBAADBCABAA', scores=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], total=2), Student(name=56753, answers='DBDDBBCBACDBCBCCCBCA', scores=[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], total=2), Student(name=60945, answers='CDDDABDADADADCCABCCD', scores=[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], total=2), Student(name=61380, answers='DABACBCABACBBDCBBAAA', scores=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], total=2)]))


##########d.1a###########

Grade= ['A', 'B', 'C', 'D']

def calculate_GPA(listofstrings):
    count=0
    for letter in listofstrings:
        if letter == 'A':
            count+=4
        elif letter == 'B':
            count+=3
        elif letter == 'C':
            count+=2
        elif letter == 'D':
            count+=1
    return count / len(listofstrings)
print(calculate_GPA(Grade))

##########d.1b###########

dictionary={'A+': 4, 'A-': 3.7, 'A': 3.3, 'B+': 3, 'B-': 2.7, 'C': 2, 'D': 1, 'F': 0}

def calculate_GPA2(lists):
    count=0
    for key in lists:
        count+= dictionary[key]
    return count/len(lists)

print(calculate_GPA2(['A+', 'A-', 'A', 'B+', 'B-']))

##########d.2###########

def flatten_2D_list(table):
    x=[]
    for item in table:
        x.extend(item)
    return x
        
assert flatten_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]) == [1, 3, 2, 3, 5, 1, 7, 5, 1, 3, 2, 9, 4]
print(flatten_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]))


##########d.3a###########

L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise', 'correctly', '534523423', 
		 'this', 'should', '1044323', 'be', 'readable']

def skip_every_third_item(aList):
    for item in range(len(aList)):
        if (item+1) % 3 != 0:
            print(aList[item])
##skip_every_third_item(L)
            

##########d.3b###########

def skip_every_nth_item(aList, integer):
    for item in range(0, len(aList)):
        if (item+1) % integer != 0:
            print(aList[item])
skip_every_nth_item(L, 3)


##########d.4a###########

work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

def tally_days_worked(aList):
    dictionary = {}
    for employee in aList:
        if employee in dictionary:
            dictionary[employee] +=1
        else:
            dictionary[employee] = 1
    return dictionary
##assert tally_days_worked == {'Kyle': 3, 'Larry': 3, 'Bob': 2, 'Brenda': 2, 'Samantha': 3, 'Jane': 4}
print(tally_days_worked(work_week))
work_days = tally_days_worked(work_week)
print()

##########d.4b###########

hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}

def pay_employees(dic1, dic2):
    keys = list(dic1.keys())
    print(keys)
    for i in keys:
        print('{} {} ${:.2f} {} {} {} ${:.2f} {}'.format(i, 'will be paid', (dic1[i]*dic2[i])*8, 'for', dic1[i]*8, 'hours of work at', dic2[i], 'per hour.'))
            
pay_employees(work_days, hourly_wages)
print()

##########d.5###########

def reverse_dict(dictionary):
    dic = {}
    key = list(dictionary.keys())
    for index in key:
        dic.update({dictionary[index]:index})
    return dic
print(reverse_dict(hourly_wages))


        


