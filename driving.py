country= input('what nationality are you: ')
age= input('how old are you:  ')
age= int(age)
if country== 'hk':
	if age>=18:
		print('you can drive')
	else:
		print('you cannot drive')