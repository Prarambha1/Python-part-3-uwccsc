STD_NAMES =['David', 'Mary', "jon", 'Harry', 'tara', 'ram']
STD_SCORE = [21, 34,12,44,12,35]
STD_AGE = [12, 13, 16, 17, 14, 15]

highest = STD_SCORE[0]
youngest = STD_AGE[0]
youngest_location = 0

for index in range(len(STD_SCORE)):
    if highest < STD_SCORE[index]:
        highest = STD_SCORE[index]
        location = index

for index in range(len(STD_AGE)):
    if STD_AGE[index] < youngest:
        youngest = STD_AGE[index]
        youngest_location = index

print(f"The student with highest score is {STD_NAMES[location]}")
print(f"The youngest student is {STD_NAMES[youngest_location]}")
