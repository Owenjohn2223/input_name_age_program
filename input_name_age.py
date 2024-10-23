# Creating a program that ask user to input name and age
name_age_list = {}

name = input("Please input a name: ")
age = int(input("Please input the age: "))

name_age_list[name] = {
    "age" : age
}

print("__________________________")
print(f"Name:\t{name}")
print(f"Age:\t{name_age_list[name]["age"]}")
print("__________________________")
# Print error message when input is not valid

# def of valid name and age, storing collected info into array

# if Yes, ask again for input. except No, show the name and age of the oldest person