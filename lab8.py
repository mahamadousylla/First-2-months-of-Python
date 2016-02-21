print('Mahamadou Sylla ID: 61549479 and Ka Seng Hoi ID: 64264956 ICS 31 Lab sec 8. Lab Asst 8')

print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (c) ----------')
print()

print('c.1')
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

def read_menu_with_count(string):
    '''takes a string naming a file in a certain
    format, reads the file, and returns a list of dish
    structures created from the data'''
    infile = open(string, 'r')
    infile = infile.readlines()
    dish=[]
    for item in infile[1:]:
        item = item.split()
        money = item[-2].strip('$')
        money = float(money)
        Dishs = Dish(' '.join(item[0:-2]), money, item[-1])
        dish.append(Dishs)
    return dish
    infile.close()
print(read_menu_with_count('menu2.txt'))

    
print()
print('c.2')

def read_menu(string):
    '''takes as argument a string, reads the file, and
    returns a list of dish structures created from the data'''
    infile = open(string, 'r')
    infile = infile.readlines()
    dish=[]
    for item in infile:
        item = item.split()
        money = item[-2].strip('$')
        money = float(money)
        Dishs = Dish(' '.join(item[0:-2]), money, item[-1])
        dish.append(Dishs)
    return dish
    infile.close()
print(read_menu('menu3.txt'))

Dish_tuples = [Dish(name='Cheese Enchiladas', price=3.5, calories='400'), Dish(name='Wet Burrito', price=6.0, calories='700'), Dish(name='Chile Relleno', price=4.0, calories='600'), Dish(name='Taco Salad', price=4.0, calories='400'), Dish(name='Beef Taco', price=1.5, calories='250'), Dish(name='Menudo', price=5.0, calories='750')]

print()
print('c.3')

def write_menu(list_of_namedtuple, string):
    ''' takes in a list of dish namedtuples and a string
    that names a file, then write the dish namedtuples to the new file'''
    outfile = open(string, 'w')
    outfile.write(str(len(list_of_namedtuple))+'\n')
    for dish in list_of_namedtuple:
        outfile.write(('{:18} ${:.2f} {}'.format(dish.name, dish.price, dish.calories))+ '\n')
    outfile.close()
write_menu(Dish_tuples, 'newfiles')


print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (d) ----------')
print()

print('d.1')

Course = namedtuple('Course', 'dept num title instr units')
  # Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = namedtuple('Student', 'ID name level major studylist')
  # All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])
sY = Student('51223344', 'Anteater, Huey', 'FR', 'CSE', [ics31, wr39a, bio97, mgt1])
sA = Student('61223344', 'Anteater, Dewey', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sB = Student('71223344', 'Programmer, Mike', 'FR', 'SE', [ics32, wr39a, bio97])
sC = Student('81223344', 'Programmer, John', 'SR', 'BIM', [ics32, mgt1])
sD = Student('91223344', 'Anteater, Jason', 'FR', 'INFX', [ics31, wr39a, bio97, mgt1])
sE = Student('01223344', 'Anteater, Lincoln', 'SO', 'CSG', [ics31, wr39b, bio97, mgt1])
sF = Student('23223344', 'Programmer, X', 'SR', 'ICS', [ics32, wr39a, bio97])
sG = Student('981223344', 'Programmer, Mack', 'SR', 'SE', [ics32, mgt1])
  
StudentBody = [sW, sX, sY, sZ, sY, sA, sB, sC, sD, sE, sF, sG]
  
def Students_at_level(list_of_students, string):
    '''takes in a list of students and a string representing class level.
    if student's class level match string, it return a list of those students'''
    x=[]
    for student in list_of_students:
        if student.level == string:
            x.append(student)
    return x
print(Students_at_level(StudentBody, 'FR'))

print()
print('d.2')

def Students_in_majors(list_of_students, list_of_strings):
    '''takes a list of students and a list of strings. if
    the students major is in the list of strings that represent majors
    it will be returned in a list'''
    x=[]
    for student in list_of_students:
        if student.major in list_of_strings:
            x.append(student)
    return x
print(Students_in_majors(StudentBody, ['PSB', 'CS']))
print()
print(Students_in_majors(StudentBody, ['COG SCI', 'PSB']))

print()
print('d.3')

def Students_in_class(list_of_students, dept_name, course_num):
    '''takes in a list of strings and a dept name and course name,
    returns a list of those students who are enrolled in the specified class'''
    x=[]
    for student in list_of_students:
        for course in student.studylist:
            if dept_name == course.dept and course_num == course.num:
                x.append(student)
    return x
print(Students_in_class(StudentBody, 'ICS', '31'))
print()
print(Students_in_class(StudentBody, 'Management', '1'))

##########This works too. This is use of multiple functions############

##def Course_equals(c1: Course, c2: Course) -> bool:
##    ''' Return True if the department and number of c1 match the department and
##	     number of c2 (and False otherwise)
##    '''
##    return c1.dept == c2.dept and c1. num == c2.num
##assert(Course_equals(ics31,ics31))
##
##def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
##    ''' Return True if the course c equals any course on the list SL (where equality
##	     means matching department name and course number) and False otherwise.
##    '''
##    return c in SL
##assert(Course_on_studylist(ics31,StudentBody[0].studylist))
##
##def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
##    ''' Return True if the course (department and course number) is on the student's
##	     studylist (and False otherwise)
##    '''
##    for course in S.studylist:
##        if course.dept == department and course.num == coursenum:
##            return True
##    return False
##assert(Student_is_enrolled(StudentBody[0],'ICS','31'))
##
##def Students_in_class(list_of_students, dept_name, course_num):
##    '''takes in a list of strings and a dept name and course name,
##    returns a list of those students who are enrolled in the specified class'''
##    x=[]
##    for student in list_of_students:
##        if Student_is_enrolled(student,dept_name,course_num) == True:
##            x.append(student)
##    return x
##print(Students_in_class(StudentBody, 'ICS', '31'))
##
##print()

print()
print('d.4')

def Student_names(list_of_students):
    '''takes in a list of students and returns a
    list of just those student's names'''
    x=[]
    for student in list_of_students:
        x.append(student.name)
    return x
print(Student_names(StudentBody))

print()
print('d.5')

ICS_Major = ['CS','CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']

def students_in_ICS(list_of_students):
    '''A list of Students who are majors from the School of ICS '''
    return(Students_in_majors(list_of_students, ICS_Major))
print(students_in_ICS(StudentBody))
print()

def majors_in_ICS(list_of_students):
    x=[]
    '''A list of the names of Students who are majors from the School of ICS'''
    return Student_names(students_in_ICS(list_of_students))
print(majors_in_ICS(StudentBody))
print()

def count_of_ICS_majors(list_of_students):
    '''The number of Students who are majors from the School of ICS'''
    return len(majors_in_ICS(list_of_students))
print(count_of_ICS_majors(StudentBody))
print()

def names_of_seniors(list_of_students):
    '''A list of the names of seniors who are majors in the School of ICS'''
    A = Students_at_level(list_of_students, 'SR')
    return majors_in_ICS(A)
print(names_of_seniors(StudentBody))
print()

def number_of_seniors(list_of_seniors):
    '''The number of seniors who are majors from the School of ICS'''
    a = names_of_seniors(list_of_seniors)
    return len(a)
print(number_of_seniors(StudentBody))
print()

def percentage_for_seniors(list_of_strings):
    '''The percentage of majors from the School of ICS who are seniors'''
    a = count_of_ICS_majors(list_of_strings)
    b = number_of_seniors(list_of_strings)
    percentage = (b / a) * 100
    return percentage
print(percentage_for_seniors(StudentBody))
print()

def freshmanICS_inICS31(list_of_students):
    '''The number of freshmen who are majors from
    the School of ICS and enrolled in ICS 31'''
    count = 0
    for student in list_of_students:
        if student.level == 'FR' and ics31 in student.studylist:
            count += count_of_ICS_majors(list_of_students)
    return count
print(freshmanICS_inICS31(StudentBody))
    
def average_unit_fresh31(list_of_students):
    '''The average number of units that freshmen
    in ICS 31 are enrolled in'''
    x = []
    count=0
    for student in list_of_students:
        a = Students_in_class(list_of_students, 'ICS', '31')
    for student in a:
        if student.level == 'FR':
            x.append(student)
    for student in x:
        for course in student.studylist:
            count = count + course.units
    average = count / len(x)
    return average
            
print(average_unit_fresh31(StudentBody))
