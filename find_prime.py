import sys

# Finds and print the nth prime number in decimal
def find_prime():    
    #initially we have no prime numbers
    primes = []
    isPrime = True
    
    if (len(sys.argv) != 2):
        sys.exit(1)
    n = int(sys.argv[1])
    
    #for i in [2, all odd numbers], check if prime
    #start with 2
    primes.append(2)
    
    #now check all odd numbers > 2
    i = 3
    
    while 1:        
        #Iterate over the primes already found which are less than the square-root of i
        for f in primes:
            #For each prime in this set, f, check to see if it is a factor of i:
            #If f divides i then i is non-prime. Continue from 2 for the next i.
            if i % f == 0:
                isPrime = False
                break
            if f*f >= i: 
                break
                    
        #If no factors are found, i is prime. 
        #If i is not the nth prime we have found, add it to the list of primes. 
        if isPrime == True:            
            if (len(primes)+1 != n):
                primes.append(i)    
            #Otherwise, i is the nth prime we have found and we should return it.
            else:
                print i
                return i
        i += 2
        isPrime = True
    
    
#if we run this as a program, execute this function
if __name__ == '__main__':        
    find_prime()
