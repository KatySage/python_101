def day_numbers():
    day = int(input("Day (0-6)? "))
    if day == 0:
        print("It's Sunday!")
    elif day == 1:
        print("It's Monday!")
    elif day == 2:
        print("It's Tuesday!")
    elif day == 3:
        print("It's Wednesday!")
    elif day == 4:
        print("It's Thursday!")
    elif day == 5:
        print("It's Friday!")
    elif day == 6:
        print("It's Saturday!")
    else: 
        print("Please enter a number from 0 to 6.")

    if day == 0 or day == 6:
        print("Sleep in!")
    elif day < 6 and day > 0:
        print("Head to work!")
day_numbers()
