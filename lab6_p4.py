#Ask the user how many visitors visited the website.
#Take the visitor names (or IDs) as input one by one.
#Store the visitor names in a set to avoid duplicates.
#At the end, display:
#The list of unique visitors.
#Total number of unique visitors.

visitors = set()
n = int(input("How many visitors visited the website? "))
for i in range(n):
    name = input(f"Enter visitor {i+1} name/ID: ")
    visitors.add(name)  # Set automatically handles duplicates
print("\nUnique Visitors:")
for visitor in visitors:
    print(visitor)
print("\nTotal number of unique visitors:", len(visitors))
