# Creating a program that ask user to input name and age
name_age_list = {}

while True:
    try:
        name = input("Please input a name: ")
        age = int(input("Please input the age: "))
        
        print("__________________________")
        print(f"Name:\t{name}")
        print(f"Age:\t{age}")
        print("__________________________")

        add_more = input("Add More?(y/n): ")

        if add_more == 'n':
            break
        elif add_more != 'y':
            print("Please choose between 'y' or 'n' only")
    except:
        print("****Invalid Input****\n **Please Try Again**")


# Print error message when input is not valid

# def of valid name and age, storing collected info into array

# if Yes, ask again for input. except No, show the name and age of the oldest person