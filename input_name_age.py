user_inputs = []

# Start an infinite loop to collect user input
while True:
    try:
        # Prompt for the user's name
        name = input("Please input a name: ")
        
        # Prompt for the user's age and convert it to an integer
        age = int(input(f"Please input {name}'s age: "))
        
        # Display the entered information
        print("---------------------")
        print(f"Name:\t{name}")
        print(f"Age:\t{age}")
        print("---------------------")

        # Store the user's name and age as a tuple in the list
        user_inputs.append((name, age))
        
        # Loop to determine if the user wants to add more entries
        while True:
            add_more = input("Add More?(y/n): ").lower()
        
            if add_more == 'n':
                # If user chooses not to add more, check if there are entries
                if user_inputs:
                    oldest_name = None
                    oldest_age = None
                    
                    # Find the oldest user
                    for user in user_inputs:
                        if oldest_age is None or user[1] > oldest_age:
                            oldest_age = user[1]
                            oldest_name = user[0]
                    
                    # Display all entries
                    print("\n")
                    print("-------All Entries-------")
                    for name, age in user_inputs:
                        print(f"~ Name:{name}\tAge:{age}")
                    print("-------------------------")
                    
                    # Display the name and age of the oldest user
                    print(f"The oldest person is {oldest_name} with an age of {oldest_age}.")
                break  # Exit the inner loop if no more entries are needed
                
            elif add_more == 'y':
                break  # Exit the inner loop to add more entries
                
            else:
                # Handle invalid input for adding more entries
                print("Please choose between 'y' or 'n' only")
        
        # If user chose not to add more, exit the outer loop
        if add_more == 'n':
            break
        
    except ValueError:
        # Handle the case where age is not an integer
        print("****Invalid Input****\n<--Please Try Again-->")
