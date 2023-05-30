from datetime import date
def has_monday_11(month, year): 
    return str(date(year,month,11).strftime("%A")=='Monday')

print(has_monday_11(7,2022))
has_monday_11(6, 2022)