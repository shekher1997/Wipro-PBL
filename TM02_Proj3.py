result = {'Dhuman':[26,56,74], 'Tishta':[84,35,54], 'Utkarsh':[51,59,64], 'Shreyashi':[87,78,67]}

name = input("Enter a name: ")
if name in result:
    print("Average percentage marks is: ",(sum(result[name])//3))
else:
    print("Invalid name.")