n = int(input('1year = '))
m = int(input('2year = '))

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

for i in range(n, m+1):
    if is_leap_year(i)==True:
        print(i)
