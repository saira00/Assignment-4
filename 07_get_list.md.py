# Initialize an empty list
my_list = []

while True:
    # Ask the user to enter a value
    value = input("Enter a value: ")

    # If the input is empty, break the loop
    if value == "":
        print("Here's the list:", my_list)
        break
    
    # Add the value to the list
    my_list.append(value)
