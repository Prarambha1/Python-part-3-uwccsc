"""

SECTION 2: 2D List

"""
grades = [
    [90, 85, 92, 78],
    [88, 91, 85, 95],
    [76, 80, 82, 85]
]

#access
print("Element in second row and third column:", grades[1][2])

#change valuee
grades[2][0] = 99
print("modifies grade:", grades)

#nested loop
print("all elements in grade:")
for row in grades:
    for grade in row:
        print(grade, end=" ")
    print()

#sum of a row
row_sum = sum(grades[0])
print("sum of first row:", row_sum)

#avg in colum
column_index = 1
column_sum = sum(row[column_index] for row in grades)
column_average = column_sum / len(grades)
print("avg of second column:", column_average)

#hightst
highest_grade = max(max(row) for row in grades)
print("Highest grade:", highest_grade)

#search
search_value = int(input("Enter a number to search in grades: "))
found = any(search_value in row for row in grades)
if found:
    print(f"{search_value} was found in grades.")
else:
    print(f"{search_value} was not found in grades.")

#row sums
print("Sum of each row:")
for i, row in enumerate(grades):
    print(f"row {i + 1} sum:", sum(row))

#column avg
print("Average of each column:")
for col in range(len(grades[0])):
    col_sum = sum(row[col] for row in grades)
    col_avg = col_sum / len(grades)
    print(f"Ccolumn {col + 1} average:", col_avg)