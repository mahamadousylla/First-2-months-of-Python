##################################PART C###################################


infile = open('male.txt', 'r')
male = infile.read()

infile.close()

infile = open('female.txt', 'r')
female = infile.read()

infile.close()

outfile = open('new.txt', 'w')
combo = outfile.write(male+female)

outfile.close()

infile = open('new.txt', 'r')
combined = infile.read()
combined = combined.split('\n')

infile.close()

infile = open('surnames.txt', 'r')
surnames = infile.read()
surnames = surnames.split('\n')

infile.close()

from random import randrange

def random():
    combine = combined[randrange(len(combined))]
    combine = combine.split()
    combine = combine[0]
    return combine
print(random())

def surname():
    surname = surnames[randrange(len(surnames))]
    surname = surname.split()
    surname = surname[0]
    return surname
print(surname())

def name(integer):
    x=[]
    for number in range(integer):
        x.append('{}, {}'.format(surname(), random()))
    return x
print(name(15))
        
##################################PART D###################################

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate(number):
    return ALPHABET[number:] + ALPHABET[0:number]

def encrypt(message, n):
    if n <= 25:
        table = str.maketrans(ALPHABET, rotate(n))
        return message.lower().translate(table)
    elif n >= 26:
        table = str.maketrans(ALPHABET, rotate(n - 26))
        return message.lower().translate(table)
print(encrypt('Where are thou', 1))
print(encrypt('WHY', 1))
print(encrypt('WHY', 27))
print()

def decrypt(message, n):
    if n <= 25:
        table = str.maketrans(rotate(n), ALPHABET)
        return message.lower().translate(table)
    elif n >= 26:
        table = str.maketrans(rotate(n - 26), ALPHABET)
        return message.lower().translate(table)
print(decrypt('xifsf bsf uipv', 1))
print(decrypt('XIZ', 1))
print(decrypt('XIZ', 27))
print()


def decrypt(message, n):
    if n <= 25:
        table = str.maketrans(ALPHABET, rotate(-n))
        return message.lower().translate(table)
    elif n >= 26:
        table = str.maketrans(ALPHABET, rotate(-n+26))
        return message.lower().translate(table)
print(decrypt('xifsf bsf uipv', 1))
print(decrypt('XIZ', 1))
print(decrypt('XIZ', 27))



def Caesar_break(message):
    result = []
    count = 0
    possibleWord = ""

    for number in range(0, 26):
        result.append(decrypt(message, number))
    print(result)
    print()

    for string in result:
        localCount = 0
        for word in string.split():
            infile = open('wordlist.txt', 'r')
            wordlist = infile.read()
            wordlist = wordlist.split('\n')
            
        
            if word in wordlist:
                localCount +=1
                    
        if localCount > count:
            possibleWord = string
            count = localCount
            
            
    infile.close()
    return possibleWord
print(Caesar_break('where are you'))        


##################################PART E###################################



import string
def remove_punctuation(character):
    '''removes punctuation from character'''
    punctuation = '!"#$%&\'()*+,?-./:;<=>?@[\\]^_`{|}~'
    for punct in punctuation:
        if punct in character:
           character = character.replace(punct, "")
    return character.replace('  ', ' ')





def copy_file(string):
    
    if string == 'line_numbers':
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')

        number = 1
        for line in infile:
            outfile.write('{:2}: {}'.format(number, line))
            number +=1
        infile.close()
        outfile.close()

    elif string == 'Gutenberg trim':
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')
        start_copy = False

        for line in infile:
            if '*** START' in line:
                start_copy = True
            if '*** END' in line:
                break
            if start_copy == True:
                outfile.write(line)
        infile.close()
        outfile.close()
        

    elif string == 'statistics':
        
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')
        allLines = infile.readlines()
        for line in allLines:
            outfile.write(line)
        print(stats(allLines))
        infile.close()
        outfile.close()


    else:
        infile_name = input("Please enter the name of the file to copy: ")
        infile = open(infile_name, 'r')
        outfile_name = input("Please enter the name of the new copy:  ")
        outfile = open(outfile_name, 'w')
        for line in infile:
            outfile.write(line)
        infile.close()
        outfile.close()

        
def stats(list_of_strings):
    count = 0
    emptyLine =0
    char=[]
    x=[]
    m=[]
    for line in list_of_strings:
        count+=1

        if line == '\n':
            emptyLine+=1

        for character in line:
            if character.isspace():
                char.append(character)

        if line != '\n':
            x.append(line)

    for line in x:
        line = remove_punctuation(line)
        for character in line:
            if character != ' ':
                m.append(character)

    return('\n\n\n\n' + '{:7}   {}'.format(count, 'lines in the file') + '\n' +
    ('{:7}   {}'.format(emptyLine, 'empty lines')) + '\n' +
    ('{:9.1f} {}'.format((len(char) / count), 'average characters per line')) + '\n' +
    ('{:9.1f} {}'.format((len(m) / len(x)), 'average characters per non-empty line')))            

        
    
print(copy_file('statistics'))




