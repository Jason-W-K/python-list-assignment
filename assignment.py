# assignment.py

# 1. Create an empty list
my_list = []

# 2. Append: 10, 20, 30, 40
for num in [10, 20, 30, 40]:
    my_list.append(num)

# 3. Insert 15 at index 1 (second position)
my_list.insert(1, 15)

# 4. Extend with [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. Remove the last element
my_list.pop()

# 6. Sort ascending
my_list.sort()

# 7. Find index of value 30 and print it
index_of_30 = my_list.index(30)

print("Final list:", my_list)
print("Index of 30:", index_of_30)
