# Step 1: the list of name names
names = ["faru", "arli", "candy", "sunji", "love", "cat"]

# Step 2: the search r
search_r = input("Enter the name to search for: ")

# Step 3: Implement the search functionality
if search_r in names:
    print(f"{search_r} was found in the list.")
else:
    print(f"{search_r} was not found in the list.")