distance = input("How far would you like to travel in miles? ")
distance = int(distance)

if(distance < 3):
    print("I suggest to ride a Bycicle to your destination")
elif(distance >= 3 and distance < 300):
    print("I suggest to ride a Motor-cycle to your destination")
else:
    print("I suggest to ride a Super-car to your destination")
