x=0
while x<3:
	password= input('Enter your password: ')
	if password=='123':
		print('logged in')
		break
	else: 
		x=x+1
		print('wrong password! you have ' , 3-x , 'times left')