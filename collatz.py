# week 1 Fundamentals of data analysis notes
# the number we will perform the Collatz operations on

n = 20 #Could ask user to input later

# keep looping until we reach 1
#Assumes Collatz conjecture is true

while n != 1: #!= means not equal to
    print(n)
    #While loop - keeps running until conditon is met ie until n does not equal 1
    if n % 2 == 0: # n modulo 2 ie give me the remainder when n is divided by 2. if n is even then remainder is 0
        n = n // 2 # collatz conjecture if n is divisible by 2
        # // means integer division ie no unnecesary decimal points
    else:
        n = (3 * n) + 1 #collatz conjecture if number is not divided by 2 

print (n)

