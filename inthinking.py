"""

Section 1: Lists

"""

scores = [85, 92, 78, 95, 88]
print(scores[2]) #third element

#change 85 to 100
scores[0] = 100
print("modified:", scores)

#print all
print("all elements:")
for score in scores:
    print(score)

# Sum
total = sum(scores)
print("sum:", total)

# Avg
average = total / len(scores)
print("average:", average)

#highest
highest = max(scores)
print("highest:", highest)

#lowest
lowest = min(scores)
print("lowest score:", lowest)

#search
search_value = int(input("Enter a number to search: "))
if search_value in scores:
    print(f"{search_value} was found.")
else:
    print(f"{search_value} was not found.")

#copy
new_scores = scores.copy()
new_scores[1] = 50  #change in row list
print("original scores:", scores)
print("new scores:", new_scores)


