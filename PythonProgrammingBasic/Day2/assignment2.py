print(f"printing Day number from weekday names")
user_str = input("Enter the day name: ").lower()


if user_str == "monday":
    print("The Day is 1st")
elif user_str == "tuesday":
    print("The Day is 2nd")
elif user_str == "wednesday":
    print("The Day is 3rd")
elif user_str == "thursday":
    print("The Day is 4th")
elif user_str == "friday":
    print("The Day is 5th")
elif user_str == "saturday":
    print("The Day is 6th")
elif user_str == "sunday":
    print("The Day is 7th")
else:
    print("The Day is not available")