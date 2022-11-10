y = int(input("Insert the year you want to check: "))

def leap_year(year):
  year_by_4 = year % 4 == 0
  year_by_100 = year % 100 == 0
  year_by_400 = year % 400 == 0
  return year_by_400 or not year_by_100 and year_by_4
if leap_year(y) is True:
    print("It's a leap year")
else:
    print("It's not a leap year")
    
answer = leap_year(y)