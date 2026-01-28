"""

SECTION 3

"""
#declaration
names = []

#adding
names.extend(["Alice", "Bob", "Charlie", "David"])

#size print
print("Size of the list:", len(names))

#access
print("Second element:", names[1])

#inserting
names.insert(0, "Eve")

#removee
names.remove("Bob")

#checck
if "Charlie" in names:
    print("Charlie exists in the list.")

#traversal
print("elements:")
for name in names:
    print(name)

#clear
names.clear()

#check empty
if not names:
    print("list is now empty.")