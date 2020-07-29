title = "Canada Dry Tonic Water"
# STOP = 21

counter = 0
while counter < len(title):
    if (counter % 2) == 0 and (title[counter] != " "):
        print(title[counter], end = " ")
    counter += 1


