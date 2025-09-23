def is_leap_year(year):
    # tu código aquí 👈
    
    if (year < 0):
        return False
    else:
        return (year % 4 == 0 and year % 100 !=0 ) or (year % 100 == 0  and year % 400 == 0 )

x=is_leap_year(2024)
print(x)