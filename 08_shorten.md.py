MAX_LENGTH = 3  # You can adjust this value for testing, but it must be 3 for the autograder

def shorten(lst):
    # Continue removing items from the end until the list has MAX_LENGTH elements
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item
        print(f"Removed: {removed_item}")  # Print the item removed

# Main function to test the shorten function
def main():
    # Example list input
    my_list = ['a', 'b', 'c', 'd', 'e']
    
    print("Original list:", my_list)
    
    # Call the shorten function
    shorten(my_list)
    
    # Final list after shortening
    print("Final list:", my_list)

if __name__ == "__main__":
    main()
