# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  none

# Write a program that asks for the user's name and another piece of information.Then prints a response using both of the inputs.

name=input("What is your name?")
pets=input("How many pets do you have?")
pets=int(pets)
if pets==1:
    print("Hello", name, "with", pets, "pet.")
else:
    print("Hello", name, "with", pets, "pets.")