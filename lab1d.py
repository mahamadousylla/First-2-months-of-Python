#Mahamadou Sylla

def factorial (n: int) -> int:
    ''' Compute n! (n factorial) '''
    if n <= 0:
        return 1
    else:
        return n * factorial (n - 1)
assert factorial(0) == 1
assert factorial(5) == 120

print("120! is ", factorial(120))
print("(50*10)! is", factorial(50 * 10))
print ("5! is", factorial(5))
#print (factorial(factorial(50)))
    
