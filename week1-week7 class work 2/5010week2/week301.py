def get_minutes(hours, minutes):
    total = hours * 60 + minutes
    return total

hours = float(input("Enter hours:"))
minutes = float(input("Enter minutes:"))
totaol_minutes =get_minutes(hours,minutes)
print(totaol_minutes)

#totaol_minutes = get_minutes(3,44)
#print(totaol_minutes)