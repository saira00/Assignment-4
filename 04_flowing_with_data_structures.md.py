def add_three_copies(my_list, data):
    for _ in range(3):
        my_list.append(data)

# Main part of the program
message = input("Enter a message to copy: ")

# Create an empty list before the function call
my_list = []

# Print list before calling the function
print("List before:", my_list)

# Call the function to add 3 copies of the message
add_three_copies(my_list, message)

# Print list after calling the function
print("List after:", my_list)
