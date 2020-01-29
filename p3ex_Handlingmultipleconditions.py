# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z
first_name = input("Input your first name: ")
first_name = first_name.upper()
last_name = ""

#print(first_name)
if first_name.startswith("A") or first_name.startswith("B"):
    print("Go to Room AB")
elif first_name.startswith("C"):
    print("Go to Room CD")
else:
    last_name = input("Input your last name: ")z
    last_name = last_name.upper()
    if last_name.startswith("Z"):
        print("Go to Room Z")
    else:
        print("Go to Room OTHER")
