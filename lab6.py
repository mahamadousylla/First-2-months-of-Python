print('Mahamadou Sylla ID: 61549479 and Yuanke Zhang ID:29038610 ICS 31 Lab sec 7. Lab Asst 6')


print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (c) ----------')
print()

print('c.1')

def contains(string, string2):
    '''takes two strings. checks
    if second string occurs in first string.
    if so, returns True. Otherwise False'''
    return string2 in string
assert contains('banana', 'ana')
assert not contains('racecar', 'ck')
print(contains('apple', 'pp'))
print(contains('oranges', 'ages'))

print('\n')
print('c.2')

import string
def remove_punctuation(character):
    '''removes punctuation from character'''
    punctuation = '!"#$%&\'()*+,?-./:;<=>?@[\\]^_`{|}~'
    for punct in punctuation:
        if punct in character:
           character = character.replace(punct, "")
    return character.replace('  ', ' ')
assert remove_punctuation('I  am going home') == 'I am going home'
print(remove_punctuation('Ok%ay'))
print()
print(remove_punctuation('I ! am not & here'))

print()

def sentence_stats(string):
    '''takes in string and prints out statistics
    including number of characters, number of words,
    average word length'''
    x=[]
    print('Characters: ', len(string))
    string = remove_punctuation(string)
    num_of_words = string.split()
    print('Words: ', len(num_of_words))
    for character in string:
        if character != ' ':
            x.append(character)
    print('Average word length: ', len(x)/ len(num_of_words))
sentence_stats('I love UCI')
print()
sentence_stats('***The ?! quick brown fox:  jumps over the lazy dog.')
    
print('\n')
print('c.3')

def initials(string):
    '''takes a name and returns
    initials of that name'''
    x=''
    string = string.split()
    for item in string:
        x=x+item[0]
        x=x.upper()
    return x
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'
print(initials("mahamadou sylla"))
print(initials('Malcolm x'))
print(initials('martin luther king'))

print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (d) ----------')
print()

print('d.1')

from random import randrange

for x in range(0, 50):
    print(randrange(0, 11))

print()
for x in range(0, 50):
    print(randrange(1, 7))

print('\n')
print('d.2')

def roll2dice():
    '''random results of rolling
    two dice'''
    for x in range(0, 50):
        x1 = randrange(1, 7)
        x2 = randrange(1, 7)
        x = x1 + x2
        print(x)
roll2dice()

print('\n')
print('d.3')

def number_rolled(number, number_of_times_rolled):
    '''takes in a number and number of times dice was rolled
    and returns results in a specific format'''
    a = '{:2}:   {:2} ({:5.1f}%) {}'.format(number, number_of_times_rolled, (((number_of_times_rolled/ 200)) * 100), (number_of_times_rolled * '*'))
    print(a)
##number_rolled(2, 7)

print()

def distribution_of_rolls(number):
    '''takes in a number representing total times two dice
    were rolled and prints a chart of results in specific format'''
    x=[]
    for numbr in range(0, 200): #every number from 0 to 200
        dice1 = randrange(1, 7)
        dice2 = randrange(1, 7)
        dice_roll_total = dice1 + dice2
        x.append(dice_roll_total)
    for n in range(2, 13):
        result = number_rolled(n, x.count(n))
    result
    print('-------------------------------------')
    print('           200 rolls         ')            
distribution_of_rolls(200)
         
        

print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (e) ----------')
print()

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def rotate_alph(n):
    ALPHABE = ALPHABET[n:] + ALPHABET[0:n]
    return ALPHABE
print(rotate_alph(1))

def Caesar_encrypt(message, number):
    if number >= 26:
        A = str.maketrans(ALPHABET, rotate_alph(number- 26))
        return message.lower().translate(A)

    elif number <= 25:
        B = str.maketrans(ALPHABET, rotate_alph(number))
        return message.lower().translate(B)
    
print(Caesar_encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))
print(Caesar_encrypt('Where art thou', 1))
print(Caesar_encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 30))


def Caesar_decrypt(message, number):
    if number >= 26:
        A = str.maketrans(ALPHABET, rotate_alph(-number+26))
        return message.lower().translate(A)
    elif number <=25:
        A = str.maketrans(ALPHABET, rotate_alph(-number))
        return message.lower().translate(A)
print(Caesar_decrypt('efghijklmnopqrstuvwxyzabcd', 4))
print(Caesar_decrypt('xifsf bsu uipv', 1))
print(Caesar_decrypt('efghijklmnopqrstuvwxyzabcd', 30))

''' In acsii code '''

##def Caesar_encrypt(message, integer):
##    '''takes a message and an integer key
##    indicating how far down the alphabet to
##    find each substitute letter'''
##    x=''
##    for letter in message:
##        if integer <=25:
##            letter = chr(ord(letter) + integer)
##            x+=letter
##            x = x.lower()
##        else:
##            if integer >= 26:
##                integer = (integer - 26)
##                letter = chr(ord(letter) + integer)
##                x+=letter
##                x=x.lower()
##    return x
##assert Caesar_encrypt('ABCDEFG', 6) =='ghijklm'
##assert Caesar_encrypt('abcDEfg', 10) == 'klmnopq'
##print(Caesar_encrypt('abcdefg', 27))
##print(Caesar_encrypt('abcdefg', 10))
##print(Caesar_encrypt('Im going home in 5 minutes', 1))
##
##print()
##
##def Caesar_decrypt(message, integer):
##    '''takes a message and an integer key
##    to decipher text'''
##    x=''
##    for letter in message:
##        if integer <= 25:
##            letter = chr(ord(letter) - integer)
##            x += letter
##            x=x.lower()
##        else:
##            if integer >= 26:
##                integer = (integer - 26)
##                letter = chr(ord(letter) - integer)
##                x += letter
##                x=x.lower()
##    return x
##assert Caesar_decrypt('fdw', 3) == 'cat'
##print(Caesar_decrypt('jn!hpjoh!ipnf!jo!6!njovuft', 1))
##print(Caesar_decrypt('bcdefgh', 1))
##
##print() 
##print('''Encrypted message''')
##print(Caesar_encrypt("We're almost done with this quarter already. Time flies!", 7))
##print(Caesar_encrypt("It's TOO early to BE awake right now", 8))
##print(Caesar_encrypt('cat', 3))
##print(Caesar_encrypt("We're almost done with this quarter already. Time flies!", 33))
##print(Caesar_encrypt("It's TOO early to BE awake right now", 34))
##print(Caesar_encrypt("cat", 29))
##
##
##print()
##print('''Decrypted message''')
##print(Caesar_decrypt("^l.yl'hstvz{'kvul'~p{o'{opz'x|hy{ly'hsylhk5'[ptl'msplz(", 7))
##print(Caesar_decrypt("q|/{(|ww(mizt(|w(jm(iism(zqop|(vw", 8))                 
##print(Caesar_decrypt('fdw', 3))
##print(Caesar_decrypt("^l.yl'hstvz{'kvul'~p{o'{opz'x|hy{ly'hsylhk5'[ptl'msplz(", 33))
##print(Caesar_decrypt("q|/{(\ww(mizt(|w(jm(iism(zqop|(vw", 34))
##print(Caesar_decrypt("fdw", 29))


  
print()  # Leaves a blank line.  print('\n') leaves two blank lines.
print()
print('---------- Part (f) ----------')
print()


print('f.1')

def print_line_number(listofstrings):
    '''takes in a list of strings and prints each
    string line by line with number corresponsing to them'''
    for i in range(len(listofstrings)):
        print('{:5}:  {}'.format(i+1, listofstrings[i]))

print_line_number([ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ])

print()
#####This works too

##infile = open('labf.py', 'r')
##data = infile.read()
####print(data)
##datalines = data.split('\n')
####print(datalines)
####for i in range(len(datalines)):
####    print(i,':  ', datalines[i])
##
##infile.close()
##
##def print_line_numbers(dataline):
##    result = 0
##    for string in dataline:
##        string = remove_punctuation(string)
##        dataline[result] = string
##        result+= 1
##    for i in range(len(dataline)-1):
##        print('{:5}:  {}'.format(i+1, dataline[i]))
##print_line_numbers(datalines)


print('\n')
print('f.2')

def stats(list_of_strings):
    '''takes in a list of strings and prints out statistics about it'''
    x=0
    l = []
    i = []
    m=[]
    print('{:7}    {} '.format(len(list_of_strings), 'lines in the list'))
    for string in list_of_strings:
        if string == "":
            x = x + 1
    print('{:7}    {} '.format(x, 'empty lines'))
    for string in list_of_strings:
        string = remove_punctuation(string)
        for character in string:
            if character != " ":
                l.append(character)
    print('{:9.1f}  {} '.format((len(l)) / len(list_of_strings), 'average characters per line'))
    for string in list_of_strings:
        if string != "":
            i.append(string)
    for string in i:
        string = remove_punctuation(string)
        for char in string:
            if char != ' ':
                m.append(char)
    print('{:9.1f}  {} '.format((len(m)) / len(i), 'average character per non-empty line'))

stats([ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        ",
        "",
        ""])

print('\n')
print('f.3')

def list_of_words(list_of_strings):
    '''takes in a list of strings, removes punctuation, and returns a list
    with individual words with whitespace removed''' 
    x=[]
    for string in list_of_strings:
        string = remove_punctuation(string)
        string = string.split()
        for word in string:
            if word != ' ':
                x.append(word)
    return x
print(list_of_words([ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new !!!!nation, conceived in liberty and dedicated",
  "to the proposit'ion that al@l men %%%are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        ",
        "",
        ""]))


##import re
##    
##def list_of_words(list_of_strings):
##    x=[]
##    table = str.maketrans('!@#$%^&*()', '          ')
##    for int in range(len(list_of_strings)):
##        list_of_strings[int] = list_of_strings[int].translate(table)
##        new = list_of_strings[int].split()
##        x +=new
##    return x
##print(list_of_words([ "Four score and seven years ago, our fathers brought forth on",
##  "this continent a new !!!!nation, conceived in liberty and dedicated",
##  "to the proposit'ion that al@l men %%%are created equal.  Now we are",
##  "   engaged in a great 		civil war, testing whether that nation, or any",
##  "nation so conceived and so dedicated, can long endure.        ",
##                      ""]))
