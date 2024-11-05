students = [
    {"name": "Alice", "grades": [95, 90, 96]},
    {"name": "Bob", "grades": [80, 99, 100]},
    {"name": "Charlie", "grades": [100, 77, 96]},
]

# Function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Open a text file to write the results
with open("students_average_grades.txt", "w") as file:
    for student in students:
        # Calculate average grade for each student
        avg_grade = calculate_average(student["grades"])
        
        # Write the result to the file
        file.write(f"{student['name']} - Average Grade: {avg_grade:.2f}\n")

print("Average grades have been written to 'students_average_grades.txt'.")
