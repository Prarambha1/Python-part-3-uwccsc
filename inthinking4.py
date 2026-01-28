# Student Grades
print("grades:")
grades = [
    [85, 90, 78, 92],  # Student 1
    [88, 76, 95, 89],  # Student 2
    [92, 88, 84, 91]   # Student 3
]

for student_index, student_grades in enumerate(grades):
    average = sum(student_grades) / len(student_grades)
    print(f"student{student_index + 1}: {average:.2f}")

print("\nproducts:")
# Inventory Management
product_names = ["Laptop", "Mouse", "Keyboard"]
product_prices = [1200.00, 25.50, 75.00]

product_name = input("name? ")
if product_name in product_names:
    product_index = product_names.index(product_name)
    print(f"{product_name}: ${product_prices[product_index]:.2f}")
else:
    print("nope.")

print("\nwords:")

# Word Frequency Counter
sentence = input("say: ")
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")