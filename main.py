# nested logic problem from Hackerrank


#actual  dd/mm/yy the book was returned
actual_day,actual_month,actual_year = map(int, input().split())

#expected dd/mm/yy the book was expected to be returned
expected_day,expected_month,expected_year = map(int, input().split())

#check if book is due, and calculate fine
if(actual_year > expected_year): # one or more years later
	fine = 10000
elif(actual_year < expected_year): # one or more years earlier
	fine = 0
else:
	if(actual_month < expected_month): # same year but earlier 
		fine = 0
	elif(actual_month > expected_month): # the book is due a few months
		fine = (actual_month - expected_month) * 500
	else:
		if(actual_day <= expected_day): # same month but earlier
			fine = 0
		else: # the book is due a few days
			fine = (actual_day - expected_day) * 15
		

print(fine) # finally, print fine