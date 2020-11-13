month = int(input('month = '))

def season(month):
    if (month == 3) or (month == 4) or (month == 5):
        return('spring')
    if (month == 6) or (month == 7) or (month == 8):
        return('summer')
    if (month == 9) or (month == 10) or (month == 11):
        return('autumn')
    if (month ==12) or (month == 1) or (month == 2):
        return('winter')

print(season(month))


