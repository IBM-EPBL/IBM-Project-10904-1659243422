import random
import time
while True:
    Temperature = random.randint(0,150)
    Humidity = random.randint(0,100)
	
    if Temperature > 100 and Humidity > 80:
        print("Temperature : " + str(Temperature))
        print("Humidity : " + str(Humidity))
        print("Temperature and Humidity is High")
        print("Alarm On !!!")
        print(" ")
        time.sleep(2)
    else:
        print("Temperature : " + str(Temperature))
        print("Humidity : " + str(Humidity))
        print("Range is Normal")
        print(" ")
