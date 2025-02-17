### This script calculates the average of four grades and assigns a letter grade based on the average.
### Average program using if/elif/else

# Steps:
# 1. The user is prompted to enter four grades.
# 2. These grades are converted to floats and stored in variables `gradeOne`, `gradeTwo`, `gradeThree`, and `gradeFour`.
# 3. The average of the four grades is calculated.
# 4. The script then uses if/elif/else statements to assign a letter grade based on the average:
#  - A: average >= 90
#  - B: 80 <= average < 90
#   - C: 75 <= average < 80
#  - D: 70 <= average < 75
#   - F: average < 70
# 5. Finally, the script prints the average and the corresponding letter grade.

# Example Usage:

# Enter grade one: 85
# Enter grade two: 90
# Enter grade three: 78
# Enter grade four: 92
# Your average is 86.25
# You have a(n) B


gradeOne = float( input("Enter grade one: "))
gradeTwo = float( input("Enter grade two: "))
gradeThree = float( input("Enter grade three: "))
gradeFour = float( input("Enter grade four: "))

average = (gradeOne + gradeTwo + gradeThree + gradeFour) / 4

if average >= 90:
    letterGrade = "A"
elif average < 90 and average >= 80:
    letterGrade = "B"
elif average < 80 and average >= 75:
    letterGrade = "C"
elif average < 75 and average >= 70:
    letterGrade = "D"
else:
    letterGrade = "F"

print("Your average is", average)
print("You have a(n)", letterGrade)