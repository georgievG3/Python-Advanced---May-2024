numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number

    except ValueError:
        print("The variable number must be an integer")

    line = input()

while line != "Remove":

    try:
        searched_number_to_print = input()
        print(numbers_dictionary[searched_number_to_print])

    except KeyError:
        line = input()
        break

    line = input()

while line != "End":

    try:
        searched_number_to_remove = input()
        del numbers_dictionary[searched_number_to_remove]

    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)

#----------------------------------------------------------------
#SOLUTION TWO

# numbers_dictionary = {}
#
# line = input()
# while line != "Search":
#     number_as_string = line
#
#     try:
#         number = int(input())
#         numbers_dictionary[number_as_string] = number
#
#     except ValueError:
#         print("The variable number must be an integer")
#
#     line = input()
#
# line = input()
# while line != "Remove":
#     searched_number_to_print = line
#
#     if searched_number_to_print in numbers_dictionary:
#         print(numbers_dictionary[searched_number_to_print])
#
#     else:
#         print("Number does not exist in dictionary")
#
#     line = input()
#
# line = input()
# while line != "End":
#     searched_number_to_remove = line
#
#     if searched_number_to_remove in numbers_dictionary:
#         del numbers_dictionary[searched_number_to_remove]
#
#     else:
#         print("Number does not exist in dictionary")
#
#     line = input()
#
# print(numbers_dictionary)
