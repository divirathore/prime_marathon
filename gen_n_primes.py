# This program is written by Divyanshi Rathore, Bhopal, MP, India
# Program to generate inputted number of prime numbers starting from
# largest prime already in the file <filename> and not more than 20000000 at time
# Also displays stored largest prime number and largest pair of twin primesThis 

import numpy
import os.path

filename = str(input("Enter the file name : "))

fe = False
pnum = 0
i = 0
fe = os.path.isfile(filename)
if (not fe):
    print("No such file as ", filename, "exists")
    print("Creating file :",filename)
    dfile = open(filename,"w")
    dfile.close()
    pnum = 0
    p_arr = numpy.zeros(pnum+20000000,int)
else:
    dfile = open(filename,"r")
    for line in dfile:
        i += 1;
    dfile.close()
    pnum = i
    p_arr = numpy.zeros(pnum+20000000,int)
    dfile = open(filename,"r")
    i = 0
    for line in dfile:
        if (i < pnum):
            word = line.split()
            p_arr[i] = int(word[0])
            i += 1;
        else:
            print("Numpy array has exhausted, there are more number of primes")
            dfile.close()
            exit()
    dfile.close()

tp_found = False
if (pnum > 0):
    nextprime = p_arr[pnum-1]
    print("Total number of prime numbers in the file is: ", pnum)
    print("Present largest prime in the file is:",nextprime)
    i = pnum - 1
    while ((tp_found == False) and (i > 1)):
        if ( p_arr[i] == (p_arr[i-1] + 2)):
            tp_found = True
        i = i - 1
    if (tp_found):
        print("Largest pair of Twin Primes in the data file is: ", p_arr[i], "and", p_arr[i+1])
    else:
        print("Database has no twin primes")
else:
    nextprime = 1

num = int(input("How many primes:"))
if (num > 20000000 or num < 1):
    print("Give greater than 0 and less than equal to 20000000")
    exit()

count = 0
chkupto = 0
prime = True
    
dfile = open(filename,"a")
while (count < num):
    if (nextprime <= 1) :
        nextprime = 2
    elif (nextprime == 2) :
        nextprime = 3
    else :
        nextprime += 2
        chkupto = int(nextprime ** (0.5))
        i = 1
        while ((p_arr[i] <= chkupto) and (prime)):
            rem = nextprime % p_arr[i]
            if (rem == 0):
                prime = False
            i += 1
    if (prime) :
        dfile.write(str(nextprime)+'\n')
        p_arr[count + pnum] = nextprime
        count += 1
    prime = True
dfile.close()
