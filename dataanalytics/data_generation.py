import random
import statistics

# Generate our Star Wars / Jane Austen character names
names = [
    "Darcy Skywalker",
    "Elizabeth Kenobi",
    "Wickham Solo",
    "Bingley Calrissian",
    "Jane Organa",
    "Lydia Fett",
    "Colonel Vader",
    "Emma Amidala",
    "Knightley Windu",
    "Harriet Tano",
    "Elliot Ren",
    "Anne Syndulla",
    "Wentworth Thrawn",
    "Marianne Andor",
    "Edward Mandalorian",
    "Elinor Jinn",
    "Willoughby Boba",
    "Catherine Ahsoka",
    "Henry Dooku",
    "Eleanor Hux",
    "Edmund Palpatine",
    "Fanny Grievous",
    "Mary Maul",
    "Margaret Phasma",
    "Brandon Ackbar"
]

# Function to generate random grades with a mean around 85% (B grade)
def generate_grade(min_grade=70, max_grade=100):
    # We'll skew the distribution to have a median around 85
    # Using a beta-like distribution by taking max of multiple uniform distributions
    a = random.uniform(min_grade, max_grade)
    b = random.uniform(min_grade, max_grade)
    return round(max(a, b))

# Create header row for CSV
csv = "Student Name,Quiz 1,Quiz 2,Quiz 3,Quiz 4,Test 1,Test 2,Project 1,Project 2,Project 3,Final Exam,Overall\n"

# Store all overall grades to calculate median later
overall_grades = []

# Generate grades for each student
for name in names:
    # Generate random grades
    quiz1 = generate_grade(65, 100)
    quiz2 = generate_grade(65, 100)
    quiz3 = generate_grade(65, 100)
    quiz4 = generate_grade(65, 100)
    test1 = generate_grade(70, 100)
    test2 = generate_grade(70, 100)
    project1 = generate_grade(75, 100)
    project2 = generate_grade(75, 100)
    project3 = generate_grade(75, 100)
    final_exam = generate_grade(70, 100)
    
    # Calculate overall grade
    # Weighted: Quizzes 20% (5% each), Tests 30% (15% each), Projects 30% (10% each), Final 20%
    overall = round(
        (quiz1 * 0.05) + 
        (quiz2 * 0.05) + 
        (quiz3 * 0.05) + 
        (quiz4 * 0.05) + 
        (test1 * 0.15) + 
        (test2 * 0.15) + 
        (project1 * 0.10) + 
        (project2 * 0.10) + 
        (project3 * 0.10) + 
        (final_exam * 0.20)
    )
    
    overall_grades.append(overall)
    
    # Add row to CSV
    csv += f"{name},{quiz1},{quiz2},{quiz3},{quiz4},{test1},{test2},{project1},{project2},{project3},{final_exam},{overall}\n"

# Calculate and display median overall grade
overall_grades.sort()
median = statistics.median(overall_grades)

print("Generated Gradebook CSV:")
print(csv[:500] + "...")  # Show just a preview
print(f"\nMedian overall grade: {median}")
print(f"Min overall grade: {min(overall_grades)}")
print(f"Max overall grade: {max(overall_grades)}")

# Calculate grade distribution
grade_ranges = {
    'A (90-100)': 0,
    'B (80-89)': 0,
    'C (70-79)': 0,
    'D (60-69)': 0,
    'F (below 60)': 0
}

for grade in overall_grades:
    if grade >= 90:
        grade_ranges['A (90-100)'] += 1
    elif grade >= 80:
        grade_ranges['B (80-89)'] += 1
    elif grade >= 70:
        grade_ranges['C (70-79)'] += 1
    elif grade >= 60:
        grade_ranges['D (60-69)'] += 1
    else:
        grade_ranges['F (below 60)'] += 1

print("\nGrade Distribution:")
for range_name, count in grade_ranges.items():
    percentage = round((count / len(overall_grades)) * 100)
    print(f"{range_name}: {count} students ({percentage}%)")

# Write the CSV to a file
with open("star_wars_austen_gradebook.csv", "w") as f:
    f.write(csv)

print("\nCSV file 'star_wars_austen_gradebook.csv' has been created.")