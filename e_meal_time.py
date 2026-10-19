def main():
    time = input("What time is it: ")
    meal_time = convert(time)
    if 7 <= meal_time <= 8:
        print("Breakfast time")
    elif 12 <= meal_time <= 13:
        print("Lunch time")
    elif 18<= meal_time <= 19:
        print("Dinner time")
# converts time in to minutes to see if it fits in the meal_time range---------------------------------------------------------
def convert(z):
    hours, minutes = z.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes / 60) # this line is doing the division first
    
main()
