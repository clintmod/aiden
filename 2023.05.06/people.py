# Create a program that reads a text file containing a list of names and their corresponding ages. T
# he program should then sort the names alphabetically and print them along with their ages in the format "Name: age".

# After that, the program should ask the user to enter a name. If the name exists in the list,
#  the program should print the age of that person.
#  If the name doesn't exist, the program should print a message saying that the name was not found.

# Finally, the program should calculate and print the average age of all the people in the list.

Name = input("Enter your name ")
people = {}
with open('people') as file:
    for line in file:
        parts = line.strip().split(': ')
        people[parts[0]] = int(parts[1])

    
print(people)
if Name in people:
    print (people[Name])
else:
    print ("Name was not found")

numbers = people.values()
# calculate the sum of numbers
total=sum(numbers)
#calculate the average
average = total / len(numbers)
print("the sum is",total)
print("The average is",average)
