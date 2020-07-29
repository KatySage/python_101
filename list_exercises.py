list_of_numbers = [1, 4, 6, 5, 7, 9]
i = 0
sum = 0
while i < len(list_of_numbers):
    sum += list_of_numbers[i]
    i +=1
print(sum)

list_of_numbers.sort()
# makes list into ascending order
print(list_of_numbers[len(list_of_numbers) -1])
#prints the highest number
print(list_of_numbers[0])
#prints the lowest number

# def even_numbers():
#     list_of_numbers2 = [-2, -1, 0, 2, 6, 9, 7]
#     even_list = []
#     for number in list_of_numbers2:
#         if number % 2 == 0:
#             even_list.append(number)
#     print(even_list)
# even_numbers()

def positive_numbers():
    list_of_numbers2 = [-2, -1, 0, 2, 6, 9, 7]
    for number in list_of_numbers2:
        if number > 0:
            print(number, end=" ")

positive_numbers()

def even_numbers():
    list_of_numbers2 = [-2, -1, 0, 2, 6, 9, 7]
    for number in list_of_numbers2:
        if number % 2 == 0:
            print(number, end=" ")
even_numbers()

def positive_numbers():
    list_of_numbers2 = [-2, -1, 0, 2, 6, 9, 7]
    pos_list = []
    for number in list_of_numbers2:
        if number > 0:
            pos_list.append(number)
    print(pos_list)
positive_numbers()


def multiply_numbers():
    list_of_numbers2 = [-2, -1, 0, 2, 6, 9, 7]
    factor = 4
    multiplied_list = []
    for number in list_of_numbers2:
        new_number = factor * number
        multiplied_list.append(new_number)
    print(multiplied_list)
multiply_numbers()

new_string = "Hello, I am a string."
print((new_string)[::-1])

list_of_numbers2 = [-2, -1, 0, 2, 6, 9, 7]

list_of_numbers2.reverse()
print(list_of_numbers2)