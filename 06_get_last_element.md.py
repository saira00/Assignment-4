def get_last_element(lst):
    # Print the last element in the list
    print(lst[-1])

# Main code to input the list
n = int(input("Enter the number of elements in the list: "))
my_list = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    my_list.append(element)

# Call the function to get the last element
get_last_element(my_list)
