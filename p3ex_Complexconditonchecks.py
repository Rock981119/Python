# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name

# Ask the user for their last name

# if first name is < 10 characters and last name is < 10 characters 
#       print first and last name on the jersey
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName

first_name = input("Input your first name: ")
last_name = input("Input your last name: ")
first_name_init = first_name[0:1].upper()
last_name_init = last_name[0:1].upper()

if len(first_name) < 10 and len(last_name) < 10:
    print(f"{first_name} {last_name}")
elif len(first_name) >= 10 and len(last_name) < 10:
    print(f"{first_name_init} {last_name}")
elif len(first_name) < 10 and len(last_name) >= 10:
    print(f"{first_name} {last_name_init}")
elif len(first_name) >= 10 and len(last_name) >= 10:
    print(f"{last_name}")
