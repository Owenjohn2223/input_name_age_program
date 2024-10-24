# Creating a program that ask user to input name and age
user_inputs = []

while True:
    try:
        name = input("Please input a name: ")
        age = int(input(f"Please input {name}'s age: "))
        
        print("__________________________")
        print(f"Name:\t{name}")
        print(f"Age:\t{age}")
        print("__________________________")

        user_inputs.append((name, age))
        
        while True:
            add_more = input("Add More?(y/n): ")
            
            if add_more == 'n':
                print("-------All Entries------")
                for name, age in user_inputs:
                    print(f"~ Name:{name}\tAge:{age}")
                print("------------------------")
                break
            elif add_more == 'y':
                break
            else:
                 print("Please choose between 'y' or 'n' only")
                 
        if add_more == 'n':
            break
        
# Print error message when input is not valid
    except ValueError:
        print("****Invalid Input****\n --Please Try Again--")

# def of valid name and age, storing collected info into array

# if Yes, ask again for input. except No, show the name and age of the oldest person