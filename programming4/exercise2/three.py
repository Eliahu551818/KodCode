hour = input("Enter Hour: ")
minute = input("Enter Minute: ")

while not hour.isdigit() or not minute.isdigit():
    hour = input("Enter Hour: ")
    minute = input("Enter Minute: ")

hour_as_int = int(hour)
hours_as_minutes = hour_as_int*60
minutes_as_int = int(minute)

print("the distance from modnight in minutes: ",hours_as_minutes+minutes_as_int)

