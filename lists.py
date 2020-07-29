alcoholic_drinks = ["Gin and Tonic", "Wine", "Beer", "Dark and Stormy", "Manhattan"]
# print(alcoholic_drinks[0])
# print(len(alcoholic_drinks[1]))

def list_drinks():
    count = 0
    while count < len(alcoholic_drinks):
        print(alcoholic_drinks[count])
        count += 1
list_drinks()
alcoholic_drinks.append("Mimosa")
list_drinks()

for drink in alcoholic_drinks:
    print(drink)