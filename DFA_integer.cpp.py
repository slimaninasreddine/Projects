# ([0-9]|[a-z]|.)*@([0-9]|[a-z]|.)*.[a-z]*


#include <iostream>
#include <string>
using namespace std

class DFA_illegal_character():
	print ("Illegal Character");
class DFA():
	def SetInitial():
		state=0
	def Step(c):
		if (state==0):
			if (c in '+' or c=='-' or c=='.'):
				state=1
			else:
			if (c>='0' and c<='9'):
				state=2
			else:
				DFA_illegal_character()
		else:
		if (state==1):
			if (c=='+' or c=='-'):
				state=3
			else:
			if (c>='0' and c<='9'):
				state=2
			else:
				DFA_illegal_character()

		else:
		if state==2:
			if c=='+' or c=='-':
				state=3
			else:
			if c>='0' and c<='9':
				state=4
			else:
				DFA_illegal_character()

		else:
		if state==3:
			if c=='+' or c=='-':
				state=3
			else:
			if c>='0' and c<='9':
				state=3
			else:
				DFA_illegal_character()

		else:
		if state==4:
			if c=='+' or c=='-':
				state=3
			else:
			if c>='0' and c<='9':
				state=4
			else:
				DFA_illegal_character()
		else:
			DFA_illegal_character()

	def IsFinal()
		return state==2 or state==4

public:
	bool IsAccepted( string &s)
		SetInitial()
		for(unsigned int i=0; i<s.size(); i++)
		Step(s[i])
		return IsFinal()




	try		if DFA().IsAccepted(s):
			cout<<"Accepted.\n"
		else:
			cout<<"Not accepted.\n"

	catch(DFA_illegal_character)		cerr<<"Illegal character in input.\n"

return 0


""" EMAIL VALIDATION """


def validate_email(user_email):
    # regex expression to use
    reg = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    # compile regex into pattern
    pattern = re.compile(reg)

    # using pattern to search the input string and validating condition
    if pattern.search(user_email):
        return 'Email is valid.'
    else:
        return 'Email is not valid. Try again!'




#([0-9]|[a-z]|.)*@([0-9]|[a-z]|.)*.[a-z]*
user_email = input('Enter your email: ')
try:
  # Validate & take the normalized form of the email ([0-9]|[a-z]|.)*@([0-9]|[a-z]|.)*.[a-z]*
  print(validate_email(user_email))
except EmailNotValidError as e:
  # email is not valid, exception message is human-readable
  print('Email is not valid. Try again!')