# Creating a program that ask user to input name and age
user_inputs = []

while True:
    try:
        name = input("Please input a name: ")
        age = int(input(f"Please input {name}'s age: "))
        
        print("---------------------")
        print(f"Name:\t{name}")
        print(f"Age:\t{age}")
        print("---------------------")

        # def of valid name and age, storing collected info into array
        user_inputs.append((name, age))
        
        while True:
            add_more = input("Add More?(y/n): ").lower()
        
        # if Yes, ask again for input. except No, show the name and age of the oldest person
            if add_more == 'n':
                if user_inputs:
                    oldest_name = None
                    oldest_age = None
                    
                    for user in user_inputs:
                        if oldest_age is None or user[1] > oldest_age:
                            oldest_age = user[1]
                            oldest_name = user[0]
                    print("\n")
                    print("-------All Entries------")
                    for name, age in user_inputs:
                        print(f"~ Name:{name}\tAge:{age}")
                    print("------------------------")
                    print(f"The oldest person is {oldest_name} with an age of {oldest_age}.")
                break
            elif add_more == 'y':
                break
            else:
                 print("Please choose between 'y' or 'n' only")
        if add_more == 'n':
            break
        
# Print error message when input is not valid
    except ValueError:
        print("****Invalid Input****\n<--Please Try Again-->")