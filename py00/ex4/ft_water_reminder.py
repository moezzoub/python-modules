def ft_water_reminder():
    day_since_lw = int(input("Days since last watering: "))
    if day_since_lw > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
