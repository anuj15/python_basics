def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        if month == 2:
            return 29
    else:
        return month_days[month - 1]


y = int(input('Enter the year: '))
m = int(input('Enter the month: '))
d = days_in_month(y, m)
print(d)
