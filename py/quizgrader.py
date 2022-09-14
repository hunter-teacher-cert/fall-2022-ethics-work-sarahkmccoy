# quizgrader.py
# Sarah McCoy
# CSCI 77800 Fall 2022
# collaborators: from Math for America workshop 5 years ago
# consulted: n/a


'''
   Display the number of correct responses using the lists
   answer_key and student_responses.
   
'''

answer_key = ['g','f','d','i','b','c','a','h','g','e']
student_responses =['g','c','d','f','b','h','j','i','g','e']
response=0
number_correct=0
for i in answer_key:
	if i == student_responses[response]:
		number_correct=number_correct + 1
	response = response + 1
print ("You answered "+ str(number_correct) + " out of "+ str(response) + " correctly! Thats " + str(number_correct/response*100) + "%")
	
'''	
Here's another way to code this...nicer perhaps
for index in range(len(answer_key)):
 if answer_key[index]==student_responses[index]:  yada yada
'''
	 