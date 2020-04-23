print("Hosting charges per hour ${}.".format(0.51))

perHour = 0.51
perDay = 24*perHour
perWeek = 7*perDay
perMonth = 30*perDay

print("\nCost per day = ${}.\nCost per Week = ${}.\nCost per Month = ${}" .format(perDay, perWeek, perMonth))
print("Number of days that could be operated with $918 are", int(918//perHour))