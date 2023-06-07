def hours_ahead():
	'''Asks the user for an hour between 1 and 12, asks them to enter am or pm,
	   and asks them how many hours into the future they want to go. 
   	   Returns what the hour will be that many hours into the future.'''

	input_hour = int(input('Enter hour between 1 and 12:\n'))
	if (input_hour < 1) | (input_hour > 12):
		print('The hour is not between 1 and 12')
		input_hour = int(input('Enter hour between 1 and 12:\n'))
	am_pm = input('AM(1) or PM(2)\n')
	if am_pm not in ['1','2']:
		print('Please enter 1 (AM) or 2 (PM).')
		am_pm = input()
	output_hour = 1
	if input_hour == 12 and am_pm == '1':
		output_hour = 0
	elif input_hour == 12 and am_pm == '2':
		output_hour = 12 
	elif am_pm == '1':
		output_hour = input_hour
	elif am_pm == '2':
		output_hour = input_hour + 12

	hours_adead = int(input('How many hours ahead?\n'))
	new_hour = 0
	new_hour = output_hour+hours_adead
	while new_hour > 23:
		new_hour = new_hour - 24

	if new_hour >=0 and new_hour < 12:
		if new_hour == 0:
			new_hour = 12
		new_hour = new_hour
		print(new_hour, 'AM')
	else:
		if new_hour == 12:
			new_hour = 12
		new_hour = new_hour - 12
		print(new_hour, 'PM')


hours_ahead()


