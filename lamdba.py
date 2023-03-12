# List of dictionaries
people = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30},
    {'name': 'Bob', 'age': 20},
    {'name': 'Mary', 'age': 27}
]

# Sort the list of dictionaries based on the 'age' key using lambda function
sorted_people = sorted(people, key=lambda x: x['age'])

# Print the sorted list of dictionaries
print(sorted_people)