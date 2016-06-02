# nested logic problem from Hackerrank


#actual  dd/mm/yy the book was returned
actual_day,actual_month,actual_year = map(int, input().split())

#expected dd/mm/yy the book was expected to be returned
expected_day,expected_month,expected_year = map(int, input().split())

#check if book is due, and calculate fine
fine = 0

if(actual_year > expected_year):
	fine = 10000
elif(actual_month > expected_month):
	fine = (actual_month - expected_month)*500
elif(actual_day > expected_day):
	fine = (actual_day - expected_day)*15



print(fine) # finally, print fine