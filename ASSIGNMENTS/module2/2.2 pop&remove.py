# Creating a list
my_list = [10, "Python", 3.14, "AI", 50, "Data"]
print("Original list:", my_list)
# Using remove() - removes element by value
my_list.remove("AI")
print("After remove('AI'):", my_list)
# Using pop() - removes element by index
my_list.pop(2)   # removes element at index 2
print("After pop(2):", my_list)
# Using pop() without index (removes last element)
my_list.pop()
print("After pop():", my_list)