def n_to_m():
    start_num = int(input("Pick a starting number: "))
    end_num = int(input("Pick an ending number: "))
    if end_num < start_num:
        print("Please try again and pick a higher number to end with.")
    while start_num <= end_num:
        print(start_num)
        start_num +=1
n_to_m()