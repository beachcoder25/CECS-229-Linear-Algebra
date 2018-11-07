#Student Name: Jonah Cornish

from math import pi,e
from plotting import plot

#Problem 1
def shift_cipher(L, key):
    return [(x + key) % 26 for x in L]

#Problem 2
def my_lists(L,num):
    return [([(z - num) for z in range(1, L[d] + 1)]) for d in range(len(L))]

#Problem 3
def myAvg(L):
    current = 0
    for x in L:
        current = x + current
    return current / len(L)

#Problem 4
#Write your code here.
#Note: Since it will use the plotting library from the book, I will test it from the Python
#command prompt. So don't worry if the plot doesn't work from an IDE. Make sure it works from 
#the Python command prompt though.


#L = {2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j}
plot([(((-3-2j+z)*(e**(1j*pi/3))))*(1/3) for z in L],4)

#Problem 5
def isPrime(L):
    for n in L[:]:

        if n < 2:
            L.remove(n)


        else:
            for i in range(2, n):
                if n % i == 0:
                    L.remove(n)
                    break

    return L

#Sample test cases for problems 1, 2, 3, and 5.
print(shift_cipher([7,4,11,11,14],18))

print(my_lists([1,2,4],5))
print(my_lists([0],5))

print(myAvg([2,5,3,2]))

print(isPrime([2,5,8,10,13]))



