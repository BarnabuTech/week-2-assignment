# This creates an empty list called my_list
my_list = []

# This appends the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # Index 1 is the second position

# Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element from my_list
my_list.pop()  # Removes the last element (70)

# Sorting my_list in ascending order
my_list.sort()

# Finding and printing the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Printing the final list to verify
print("Final my_list:", my_list)