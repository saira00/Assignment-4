def get_first_element(lst):
    # Print the first element in the list
    print(lst[0])

# Main code to input the list
n = int(input("Enter the number of elements in the list: "))
my_list = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    my_list.append(element)

# Call the function to get the first element
get_first_element(my_list)
