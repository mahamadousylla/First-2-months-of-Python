print('Mahamadou Sylla')

print('\n\n\n\n')

##################STAGE 1##################

infile = open('input_file.txt', 'r')
bedrooms = infile.readlines()

infile.close()

variationNB = ['NB', 'Nb', 'nB', 'nb']
variationLB = ["LB" , "lb" , "Lb" , "lB"]
variationPL = ["PL" , "pl" , "Pl" , "pL"]

rooms=[]

def globalFunction(listoflines):
    for line in listoflines:
        if line.split()[0] in variationNB:
            new_line = line.split()[1:]
            rooms.extend(new_line)

        if line.split()[0] in variationLB:
            print('Number of bedrooms in service: ', len(rooms))
            print('-' * 36)
            for n in rooms:
                print(n)

        if line.split()[0] in variationPL:
            new = line.split()[1:]
            print(' '.join(new))
            
globalFunction(bedrooms)
