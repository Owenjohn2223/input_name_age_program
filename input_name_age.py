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

        user_inputs.append({'name': name, 'age': age})

        add_more = input("Add More?(y/n): ")

        if add_more == 'n':
            break

        elif add_more != 'y':
           print("Please choose between 'y' or 'n' only")

# Print error message when input is not valid
    except ValueError:
        print("****Invalid Input****\n --Please Try Again--")

# def of valid name and age, storing collected info into array

# if Yes, ask again for input. except No, show the name and age of the oldest person
for inputs in user_inputs:
    print(inputs)