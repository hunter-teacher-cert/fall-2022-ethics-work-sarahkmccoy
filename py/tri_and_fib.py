# tri_and_fib.py
# Sarah McCoy
# CSCI 77800 Fall 2022
# collaborators: N/A
# consulted: N/A


'''
Short program that prints out triangular and fibonacci numbers
'''


print ("Here are some of the triangular numbers.  Can you figure out the pattern?")
sum = 1
add = 1
while sum <= 100:
	print (sum)
	add = add + 1
	sum = sum + add
print (sum)

print ("Now here are some Fibonacci Numbers.  Can you figure out the pattern?")
temp1=1
temp2=0
fib=0
while fib <= 200:
	print (fib)
	fib=temp1 + temp2
	temp1 = temp2
	temp2 = fib
	
	

